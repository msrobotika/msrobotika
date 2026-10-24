#!/usr/bin/env python3
"""Inventario real de los repositorios públicos de MS ROBOTIKA.

Consulta exclusivamente GitHub REST API. No ejecuta software remoto.
"""
import argparse
import base64
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import posixpath
import re
import sys
from urllib.parse import quote, unquote
from urllib.request import Request, urlopen

OWNER = "msrobotika"
API = "https://api.github.com"
OUTPUT = Path(__file__).resolve().parents[1] / "reports"
MD_LINK = re.compile(r"!?\[[^\]]*?\]\(([^)]+)\)")
HTML_LINK = re.compile(r"""(?:src|href)=["']([^"']+)["']""")
IMG = re.compile(r"\.(png|jpg|jpeg|svg|webp|gif)$", re.I)

def get(path):
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28",
               "User-Agent": "MS-ROBOTIKA-Portfolio-Audit"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urlopen(Request(API + path, headers=headers), timeout=25) as response:
        return json.load(response)

def repositories():
    result = []
    for page in range(1, 6):
        part = get("/users/" + OWNER + "/repos?type=owner&per_page=100&page=" + str(page))
        result.extend(x for x in part if x["owner"]["login"].lower() == OWNER.lower())
        if len(part) < 100:
            break
    return sorted((x for x in result if not x["private"]), key=lambda x: x["name"].casefold())

def local_links(markdown):
    links = []
    for raw in MD_LINK.findall(markdown) + HTML_LINK.findall(markdown):
        text = raw.strip().strip("<>")
        if not text or text.lower().startswith(("http:", "https:", "//", "#", "mailto:", "data:")):
            continue
        text = re.split(r'\s+["\']', text, maxsplit=1)[0]
        text = unquote(text.split("#", 1)[0].split("?", 1)[0])
        if not text or text.startswith("/"):
            continue
        links.append(posixpath.normpath(text.removeprefix("./")))
    return list(dict.fromkeys(links))

def inspect(repo):
    name = repo["name"]
    location = "/repos/" + OWNER + "/" + quote(name, safe="")
    branch = quote(repo["default_branch"], safe="")
    tree = get(location + "/git/trees/" + branch + "?recursive=1")
    if tree.get("truncated"):
        raise ValueError("Git tree truncated for " + name)
    files = {x["path"] for x in tree["tree"] if x["type"] == "blob"}
    folders = {x["path"] for x in tree["tree"] if x["type"] == "tree"}
    readme = next((x for x in files if x.casefold() == "readme.md"), None)
    broken = []
    if readme:
        item = get(location + "/contents/" + quote(readme, safe="") + "?ref=" + branch)
        md = base64.b64decode(item["content"]).decode("utf-8", "replace")
        broken = [p for p in local_links(md) if p not in files and p not in folders]
    workflows = sorted(x for x in files if x.startswith(".github/workflows/") and x.endswith((".yml", ".yaml")))
    media = sorted(x for x in files if IMG.search(x) and
                   ("/screenshots/" in x or "/captures/" in x or x.startswith("docs/")))
    head = get(location + "/commits/" + branch)["sha"]
    runs = get(location + "/actions/runs?per_page=100&branch=" + branch).get("workflow_runs", [])
    # One successful job must not hide a failed workflow, or imply that an old
    # run tested the current source revision. Keep each latest workflow visible.
    latest_by_workflow = {}
    for run in runs:
        latest_by_workflow.setdefault(run["workflow_id"], run)
    evidence = [{"name": r["name"], "sha": r["head_sha"],
                 "status": r["status"], "conclusion": r.get("conclusion"),
                 "url": r["html_url"], "current_head": r["head_sha"] == head}
                for r in latest_by_workflow.values()]
    if any(x["conclusion"] in ("failure", "timed_out", "action_required") for x in evidence):
        conclusion = "failure recorded"
    elif any(x["status"] != "completed" for x in evidence):
        conclusion = "in progress"
    elif evidence and all(x["current_head"] and x["conclusion"] == "success" for x in evidence):
        conclusion = "success at current HEAD"
    elif evidence:
        conclusion = "historical / mixed revisions"
    else:
        conclusion = "not-verified"
    latest = runs[0] if runs else None
    return {
        "repository": name, "url": repo["html_url"], "branch": repo["default_branch"],
        "readme": bool(readme),
        "license_file": any(x == "LICENSE" or x.startswith("LICENSE.") or x == "COPYING" for x in files),
        "security": "SECURITY.md" in files,
        "project_status": "docs/PROJECT_STATUS.md" in files,
        "contributing": "CONTRIBUTING.md" in files,
        "workflows": workflows, "assets": media,
        "head_sha": head, "workflow_evidence": evidence,
        "ci_conclusion": conclusion,
        "ci_url": latest.get("html_url") if latest else None,
        "broken_local_readme_links": broken,
    }

def markdown(report):
    lines = ["# MS ROBOTIKA - Informe técnico automatizado", "",
             "Generado: " + report["timestamp_utc"] + " (UTC). GitHub API / rama predeterminada.",
             "", "Repositorios públicos analizados: " + str(report["count"]),
             "", "| Repositorio | Licencia | Evidencia de CI por revisión | Recursos visuales | Enlaces locales rotos |",
             "|---|---|---|---:|---:|"]
    for r in report["repositories"]:
        ci = r["ci_conclusion"]
        if r["ci_url"]:
            ci = "[" + ci + "](" + r["ci_url"] + ")"
        lines.append("| [" + r["repository"] + "](" + r["url"] + ") | " +
                     ("Archivo" if r["license_file"] else "No consta") + " | " +
                     ci + " | " + str(len(r["assets"])) + " | " +
                     str(len(r["broken_local_readme_links"])) + " |")
    lines += ["", "## Incidencias documentales", ""]
    issues = []
    for r in report["repositories"]:
        if not r["license_file"] and r["repository"] != OWNER:
            issues.append("- " + r["repository"] + ": sin archivo de licencia. No se infiere permiso de redistribución.")
        if r["broken_local_readme_links"]:
            issues.append("- " + r["repository"] + ": referencias internas sin destino: " +
                          ", ".join(r["broken_local_readme_links"]))
        if not r["workflows"] and r["repository"] != OWNER:
            issues.append("- " + r["repository"] + ": no se encontró workflow de pruebas en main.")
    lines.extend(issues or ["No se detectaron incidencias en estas comprobaciones básicas."])
    lines += ["", "## Evidencia por workflow", "",
              "Una ejecución antigua correcta no acredita el HEAD actual. Un fallo se conserva aunque otro workflow haya pasado.", "",
              "| Repositorio | Workflow | Resultado | Revisión | HEAD actual |",
              "|---|---|---|---|---|"]
    for r in report["repositories"]:
        for w in r.get("workflow_evidence", []):
            lines.append(f"| {r['repository']} | [{w['name']}]({w['url']}) | {w['conclusion'] or w['status']} | `{w['sha'][:12]}` | {'Sí' if w['current_head'] else 'No'} |")
    lines += ["", "## Límites del informe", "",
              "- La existencia de una CI, licencia o imagen no demuestra funcionamiento, derechos de terceros ni seguridad.",
              "- Las referencias locales del README se comprueban mediante expresiones Markdown/HTML simples.",
              "- No se valida hardware físico, metrología, resultados de clasificación ni utilidad clínica.",
              "- No se realizan accesos a ficheros secretos, credenciales o repositorios privados.",
              "", "[Estándar de repositorios](../docs/REPO_STANDARD.md) / [Índice MS ROBOTIKA](../README.md).", ""]
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict-links", action="store_true")
    args = ap.parse_args()
    items, errors = [], []
    for repo in repositories():
        try:
            items.append(inspect(repo))
            print("OK", repo["name"], flush=True)
        except Exception as exc:
            errors.append({"repository": repo["name"], "error": str(exc)})
            print("ERROR", repo["name"], exc, file=sys.stderr, flush=True)
    report = {"schema": 1, "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "owner": OWNER, "count": len(items), "repositories": items, "errors": errors}
    OUTPUT.mkdir(parents=True, exist_ok=True)
    (OUTPUT / "portfolio-status.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", "utf-8")
    (OUTPUT / "portfolio-status.md").write_text(markdown(report), "utf-8")
    print("Revisados:", len(items), "errores:", len(errors),
          "enlaces rotos:", sum(len(x["broken_local_readme_links"]) for x in items))
    return 2 if errors else (1 if args.strict_links and
            any(x["broken_local_readme_links"] for x in items) else 0)

if __name__ == "__main__":
    sys.exit(main())
