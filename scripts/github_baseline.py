#!/usr/bin/env python3
"""Read-only, reproducible GitHub portfolio baseline, no external packages.
The script writes NEW baseline files only: preserves previous audit/history.
Run in Actions with a read-only token; no mutating GitHub API operations.
"""
from __future__ import annotations
import base64
import csv
from datetime import datetime, timezone
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

OWNER = "msrobotika"
DATE = "2026-10-23"
OUT = Path("reports")
UNKNOWN = "NO_VERIFICADO"
UNAVAILABLE = "NO_DISPONIBLE"
# Human evidence classification: does not mean the project passed a local smoke test.
STATUS = {
    "msrobotika": ("USABLE", "Repositorio de documentación/perfil; producto no ejecutable."),
    "AB-PLC-Simulator": ("EXPERIMENTAL", "Simulador de laboratorio con CI/E2E previo; pendiente instalación limpia y distribución validada."),
    "AB-BI-Studio": ("EXPERIMENTAL", "Release y pruebas previas; pendiente verificar descarga e inicio limpio en Windows/Linux."),
    "AB-Modbus-Studio": ("EXPERIMENTAL", "Cliente y laboratorio Modbus; release preliminar y hardware real no evaluado."),
    "-AB-Vision-Inspector": ("EXPERIMENTAL", "Inspector de laboratorio; calibración metrológica no acreditada."),
    "AB-GRAFCET-Studio-v0.1-c": ("EXPERIMENTAL", "Editor/simulador didáctico; IEC y hardware no certificados."),
    "AB-KOP-Studio-v0.1": ("EXPERIMENTAL", "Editor/simulador didáctico; PLC real no validado."),
    "AB-SCL-Studio": ("EXPERIMENTAL", "Conversor de subconjunto booleano; no cubre SCL/ST completo."),
    "AB-Serial-Analyzer-v0.1-": ("EXPERIMENTAL", "Laboratorio serie/RTU; pruebas de hardware en campo pendientes."),
    "AB-Suite-Core-arquitectura-de-integraci-n": ("EXPERIMENTAL", "Bus local y contratos con tests; sin persistencia durable ni interop industrial completa."),
    "AB-SCADA-Studio": ("IN_DEVELOPMENT", "Creado 23/10/2026; prototipo SCADA de laboratorio, NO producto terminado ni comercializable."),
    "AB-GEN-Green-AI": ("RESEARCH-AUDIT", "Cifras históricas no validadas RAW; ruta cache→RAW, leakage y lote por resolver; licencia general pendiente."),
    "AB-GEN-MEDICAL-DEMO.": ("RESEARCH-AUDIT", "Demo médica sin validación clínica; no destinada a pacientes."),
    "AgroVive-M5-Dashboard": ("RESEARCH-AUDIT", "Demo agro/visión; precisión y consumo pendientes de ensayo reproducible."),
    "Offscreen": ("EXPERIMENTAL", "Prototipo web con modelos externos; experiencia final no ensayada."),
    "MSA-BLE-Scout": ("EXPERIMENTAL", "Firmware BLE; evidencias parciales, reproducibilidad por placa pendiente."),
    "MSA-WiFi-Sentinel": ("EXPERIMENTAL", "Monitor Wi-Fi pasivo; validación de RF/cobertura limitada."),
    "MSA-ChipSafe": ("EXPERIMENTAL", "Prototipo ESP32; backup/restauración no validado por dispositivo."),
    "MSA-RogueWatch": ("EXPERIMENTAL", "Prototipo de detección, alertas no equivalen a evidencia forense."),
    "MSA-CyberDeck": ("EXPERIMENTAL", "APK de desarrollo y código main no necesariamente equivalente a la release."),
}

TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()
NOW = datetime.now(timezone.utc).isoformat(timespec="seconds")
CALLS = 0
ERRORS: list[str] = []

def api(path: str, *, optional=False):
    """Returns None on errors; never treats failed requests as empty resources."""
    global CALLS
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "msrobotika-evidence-audit/1.0",
               "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    request = Request("https://api.github.com" + path, headers=headers)
    CALLS += 1
    try:
        with urlopen(request, timeout=25) as resp:
            return json.load(resp)
    except (HTTPError, URLError, ValueError, TimeoutError) as exc:
        status = exc.code if isinstance(exc, HTTPError) else type(exc).__name__
        if not optional:
            ERRORS.append(f"{path.split('?')[0]}: {status}")
        return None

def segment(repo):
    return "/repos/" + quote(OWNER, safe="") + "/" + quote(repo, safe="")

def exists(files, *names):
    return any(x in files for x in names)

def json_string(value):
    if value is None:
        return UNKNOWN
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))

def runtime_and_dependencies(files, pack):
    types = []
    if "package.json" in files: types.append("Node.js/JavaScript")
    if any(p.endswith(".py") for p in files) or any(
            name in files for name in ("requirements.txt", "pyproject.toml")):
        types.append("Python")
    if any(p.endswith(".ino") for p in files): types.append("Arduino/C++")
    if any(p.endswith(".cpp") and ("firmware/" in p or "src/" in p) for p in files):
        types.append("C++")
    if any(p.endswith(".gradle") or p.endswith(".gradle.kts") for p in files):
        types.append("Android/Gradle")
    if exists(files, "index.html") and not types: types.append("Browser/HTML")
    locks = [x for x in ("package-lock.json", "pnpm-lock.yaml", "yarn.lock",
                         "requirements.txt", "requirements-dev.txt", "poetry.lock",
                         "Pipfile.lock", "platformio.ini", "build.gradle", "build.gradle.kts")
             if x in files]
    scripts = pack.get("scripts", {}) if isinstance(pack, dict) else {}
    start = [f"npm run {x}" for x in ("start", "dev", "test", "check")
             if isinstance(scripts, dict) and x in scripts]
    return (", ".join(dict.fromkeys(types)) or UNKNOWN,
            ", ".join(locks) if locks else UNKNOWN,
            ", ".join(start) if start else UNKNOWN)

def read_package(repo, files, base):
    if "package.json" not in files:
        return None
    raw = api(base + "/contents/package.json", optional=True)
    if not isinstance(raw, dict) or raw.get("encoding") != "base64":
        return None
    try:
        return json.loads(base64.b64decode(raw["content"]).decode("utf-8"))
    except (ValueError, KeyError):
        return None

def traffic(repo, base):
    # GitHub Traffic requires elevated per-repo access and covers a rolling 14-day window.
    out = {}
    for category in ("views", "clones", "popular/referrers", "popular/paths"):
        response = api(base + "/traffic/" + category, optional=True)
        out[category.replace("/", "_")] = response if isinstance(response, (dict, list)) else UNAVAILABLE
    return out

def audit_one(repo, info):
    base = segment(repo)
    metadata = info if isinstance(info, dict) else {}
    default = metadata.get("default_branch") or "main"
    path = base + "/git/trees/" + quote(default, safe="") + "?recursive=1"
    tree = api(path)
    tree_ok = isinstance(tree, dict) and not tree.get("truncated")
    files = {x["path"] for x in tree.get("tree", []) if isinstance(x, dict)
             and x.get("type") == "blob"} if tree_ok else set()
    pack = read_package(repo, files, base) if tree_ok else None
    runtime, dependencies, commands = runtime_and_dependencies(files, pack)
    head = api(base + "/commits/" + quote(default, safe=""), optional=True)
    head_sha = head.get("sha") if isinstance(head, dict) else None
    workflows = [p for p in files if p.startswith(".github/workflows/") and
                 (p.endswith(".yml") or p.endswith(".yaml"))]
    ci = api(base + "/actions/runs?branch=" + quote(default, safe="") +
             "&per_page=15", optional=True)
    runs = ci.get("workflow_runs", []) if isinstance(ci, dict) else []
    latest = next((r for r in runs if r.get("status") == "completed"), None)
    matching = next((r for r in runs if r.get("status") == "completed" and
                     r.get("head_sha") == head_sha), None) if head_sha else None
    releases = api(base + "/releases?per_page=10", optional=True)
    releases = releases if isinstance(releases, list) else None
    traffic_result = traffic(repo, base)
    license_obj = metadata.get("license")
    api_license = license_obj.get("spdx_id") if isinstance(license_obj, dict) else None
    license_file = next((x for x in ("LICENSE", "LICENSE.md", "LICENSE.txt",
                                     "COPYING", "COPYING.md") if x in files), None) if tree_ok else None
    original_screenshot = [p for p in sorted(files) if
                           (p.lower().endswith((".png", ".jpg", ".jpeg", ".webp")) and
                            any(k in p.lower() for k in ("screenshot", "pantalla", "capture")))]
    homepage = metadata.get("homepage")
    created, reason = STATUS[repo]
    if repo == "AB-GEN-Green-AI":
        license_status = "SIN_LICENCIA_GENERAL" if tree_ok and not license_file else UNKNOWN
    else:
        license_status = (f"{api_license} ({license_file})" if api_license and license_file
                          else f"Archivo {license_file}: contenido NO_VERIFICADO" if license_file
                          else "SIN_ARCHIVO" if tree_ok else UNKNOWN)
    row = {
        "repository": repo,
        "url": "https://github.com/" + OWNER + "/" + repo,
        "created_at": metadata.get("created_at") or UNKNOWN,
        "updated_at": metadata.get("updated_at") or UNKNOWN,
        "pushed_at": metadata.get("pushed_at") or UNKNOWN,
        "visibility": metadata.get("visibility") or
                      ("public" if metadata.get("private") is False else UNKNOWN),
        "default_branch": default,
        "head_sha": head_sha or UNKNOWN,
        "description": metadata.get("description") or "SIN_CONFIGURAR",
        "topics": metadata.get("topics") if isinstance(metadata.get("topics"), list) else UNKNOWN,
        "homepage": homepage if homepage else "SIN_CONFIGURAR",
        "stars": metadata.get("stargazers_count", UNKNOWN),
        "forks": metadata.get("forks_count", UNKNOWN),
        "open_issues": metadata.get("open_issues_count", UNKNOWN),
        "license": license_status,
        "runtime": runtime,
        "dependencies": dependencies,
        "run_commands_declared": commands,
        "ci_defined": len(workflows) if tree_ok else UNKNOWN,
        "ci_workflows": workflows if tree_ok else UNKNOWN,
        "ci_latest_completed": (f"{latest.get('conclusion','UNKNOWN')} @ {latest.get('head_sha','?')}"
                                if latest else UNKNOWN),
        "ci_at_current_head": matching.get("conclusion") if matching else UNKNOWN,
        "ci_at_current_head_url": matching.get("html_url") if matching else UNKNOWN,
        "readme": "SI" if "README.md" in files else
                  "NO" if tree_ok else UNKNOWN,
        "security": "SI" if "SECURITY.md" in files else
                    "NO" if tree_ok else UNKNOWN,
        "contributing": "SI" if "CONTRIBUTING.md" in files else
                        "NO" if tree_ok else UNKNOWN,
        "technical_status": "SI" if "docs/PROJECT_STATUS.md" in files else
                            "NO" if tree_ok else UNKNOWN,
        "screenshots_present": len(original_screenshot) if tree_ok else UNKNOWN,
        "screenshots_provenance": "NO_VERIFICADO_AUTOMATICAMENTE",
        "demo_executed_in_this_audit": "NO_VERIFICADO",
        "release_count": len(releases) if releases is not None else UNKNOWN,
        "releases": ([{"tag": r.get("tag_name"), "prerelease": r.get("prerelease"),
                       "assets": [{"name": a.get("name"), "bytes": a.get("size"),
                                   "downloads": a.get("download_count")}
                                  for a in r.get("assets", [])]}
                      for r in releases[:10]] if releases is not None else UNKNOWN),
        "tree_complete": tree_ok,
        "classification": created,
        "classification_reason": reason,
        "risks": reason,
        "traffic": traffic_result
    }
    return row

def render(value):
    if isinstance(value, (list, dict)):
        return json_string(value)
    return str(value).replace("|", "\\|").replace("\n", " ")

def make_report(rows):
    public = [r for r in rows if r["visibility"] == "public"]
    known_stars = [r["stars"] for r in rows if type(r["stars"]) is int]
    known_forks = [r["forks"] for r in rows if type(r["forks"]) is int]
    total_stars = str(sum(known_stars)) if len(known_stars) == len(rows) else UNKNOWN
    total_forks = str(sum(known_forks)) if len(known_forks) == len(rows) else UNKNOWN
    topic_none = sum(1 for r in rows if r["topics"] == [])
    homepage_none = sum(1 for r in rows if r["homepage"] == "SIN_CONFIGURAR")
    lines = [
        "# Línea base GitHub MS ROBOTIKA — 23/10/2026",
        "",
        f"**Captura UTC:** {NOW}. **Fuente:** GitHub REST API, consulta READ-ONLY desde GitHub Actions.",
        f"**Repositorios inventariados:** {len(rows)}; **públicos confirmados:** {len(public)}.",
        f"**Estrellas por repositorio (suma, NO personas únicas):** {total_stars}. **Forks:** {total_forks}.",
        f"**Sin Topics:** {topic_none} (de {len(rows)}); **sin Homepage:** {homepage_none} (de {len(rows)}).",
        "",
        "> CLAVE: NO_VERIFICADO = dato o ejecución no comprobada; NO_DISPONIBLE = endpoint Traffic sin acceso.",
        "> Un test CI 'success' no acredita ejecución de una aplicación, pruebas hardware, calidad metrológica ni validación de producto.",
        "> AB-SCADA Studio permanece IN_DEVELOPMENT, incluso si alguna prueba de laboratorio es correcta.",
        "",
        "## Inventario técnico de los 20 repositorios",
        "",
        "| Repositorio | Clasificación | Público | Último SHA | Stars | Forks | Topics | Homepage | CI en SHA | Release(s) |",
        "|---|---|---|---|---:|---:|---|---|---|---|"
    ]
    for r in rows:
        tags = "0" if r["topics"] == [] else render(r["topics"])
        lines.append(f"| [{r['repository']}]({r['url']}) | {r['classification']} | "
                     f"{r['visibility']} | {chr(96)}{r['head_sha'][:10]}{chr(96)} | {r['stars']} | {r['forks']} | "
                     f"{tags} | {r['homepage']} | {r['ci_at_current_head']} | {r['release_count']} |")
    lines += ["", "## Fichas: cobertura, arranque, riesgos y documentación", ""]
    for r in rows:
        lines += [
            f"### [{r['repository']}]({r['url']}) — {r['classification']}",
            "",
            f"**Motivo de clasificación:** {r['classification_reason']}",
            f"**Fecha creada:** {r['created_at']}; **actualizada:** {r['updated_at']}; "
            f"**último push:** {r['pushed_at']}. Rama {r['default_branch']} / SHA {r['head_sha']}.",
            f"**Descripción:** {r['description']}. **Topics:** {render(r['topics'])}. **Homepage:** {r['homepage']}.",
            f"**Licencia:** {r['license']}. **Runtime detectado por archivos:** {r['runtime']}. "
            f"**Indicadores de dependencias:** {r['dependencies']}.",
            f"**Arranque/test declarados en package.json:** {r['run_commands_declared']}. "
            "**Smoke test ejecutado para esta auditoría:** NO_VERIFICADO.",
            f"**CI configurada:** {r['ci_defined']} ({render(r['ci_workflows'])}); "
            f"**última terminada:** {r['ci_latest_completed']}; "
            f"**CI en SHA actual:** {r['ci_at_current_head']} "
            f"({r['ci_at_current_head_url']}).",
            f"**Documentos:** README {r['readme']}, SECURITY {r['security']}, "
            f"CONTRIBUTING {r['contributing']}, PROJECT_STATUS {r['technical_status']}.",
            f"**Imágenes localizadas:** {r['screenshots_present']}; **captura genuina en SHA actual:** "
            f"{r['screenshots_provenance']}. **Demo:** {r['demo_executed_in_this_audit']}.",
            f"**Releases y activos:** {render(r['releases'])}; "
            f"**issues abiertas (no exclusivas de terceros):** {r['open_issues']}.",
            f"**Riesgos/pendientes:** {r['risks']}.",
            f"**Traffic (14 días, no acumular únicos entre repos):** {render(r['traffic'])}.",
            "",
        ]
    lines += ["## Límites metodológicos", "",
        "- Las licencias de dependencias, propietarios de datasets, programas binarios y modelo clínico requieren auditorías adicionales.",
        "- Los enlaces de capturas se infieren de árboles de archivos; su autenticidad y SHA de ejecución NO se acreditan automáticamente.",
        "- No se ejecutaron programas ni pruebas físicas en esta auditoría de metadatos. La CI histórica se presenta solo como evidencia de la CI, no de un smoke test local.",
        "- El campo Homepage no se rellena automáticamente. Ningún Topic o pin se modifica en este script.",
        "- No sustituir el informe histórico docs/PORTFOLIO_AUDIT_2026-10-23.md (18 repos) ni reports/portfolio-status.md.",
        "- Dos PR abiertas preexistentes y NO duplicadas: [perfil #1](https://github.com/msrobotika/msrobotika/pull/1) y [PLC #16](https://github.com/msrobotika/AB-PLC-Simulator/pull/16).",
        "- El acceso a Insights → Traffic exige permisos del titular. En caso de 403/404 se declara NO_DISPONIBLE, nunca cero.",
        "",
        f"**Peticiones REST realizadas:** {CALLS}. **Errores registrados (sin tokens):** {len(ERRORS)}.",
    ]
    return "\n".join(lines) + "\n"

def main():
    listing = api("/users/" + OWNER + "/repos?per_page=100")
    if not isinstance(listing, list):
        raise SystemExit("ERROR: no se pudo verificar el inventario público en GitHub; no se crean cifras inventadas")
    provided = {r["name"]: r for r in listing if isinstance(r, dict) and r.get("private") is False and
                r.get("owner", {}).get("login", "").lower() == OWNER.lower()}
    if set(provided) != set(STATUS):
        print("WARN: discrepancia entre listado y clasificación: ",
              sorted(set(provided) ^ set(STATUS)))
        # Do not omit a newly found repository and claim inventory is complete.
        raise SystemExit("ERROR: inventario difiere; revisar y versionar la clasificación antes de continuar")
    rows = [audit_one(name, provided[name]) for name in STATUS]
    OUT.mkdir(parents=True, exist_ok=True)
    data = {"schema": "msrobotika.github.baseline.v1",
            "date": DATE, "captured_utc": NOW,
            "source": "GitHub REST API, metadata only", "repositories": rows,
            "errors": ERRORS}
    (OUT / "portfolio-baseline-2026-10-23.json").write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    fields = [x for x in rows[0] if x not in ("traffic", "releases", "ci_workflows")]
    with (OUT / "portfolio-baseline-2026-10-23.csv").open(
            "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: json_string(row[k]) if isinstance(row[k], (dict, list))
                             else row[k] for k in fields})
    (OUT / "GITHUB_BASELINE_2026-10-23.md").write_text(
        make_report(rows), encoding="utf-8")
    print(f"OK: {len(rows)} repositorios / {CALLS} consultas / {len(ERRORS)} errores")
    print("Creado: GITHUB_BASELINE_2026-10-23.md, portfolio-baseline-2026-10-23.csv/json")
    if ERRORS:
        print("WARN: hay datos NO_VERIFICADO (detalles en JSON); no se sustituyeron por cero.")

if __name__ == "__main__":
    main()
