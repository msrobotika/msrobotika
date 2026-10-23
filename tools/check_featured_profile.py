#!/usr/bin/env python3
"""Read-only CI: verify links, screenshot signatures and release URLs featured in profile.
This is NOT a smoke test of PLC hardware or a source-code runtime. No Github mutations.
"""
import base64
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import re
from urllib.error import HTTPError,URLError
from urllib.parse import quote
from urllib.request import urlopen,Request

OWNER="msrobotika"
REPO_FILES={
 "AB-PLC-Simulator": [
    "README.md","package.json","scripts/serve.mjs","examples/conveyor-with-fault.json",
    "docs/screenshots/lab-conveyor.png"],
 "AB-Modbus-Studio": [
    "README.md","ab_modbus/__main__.py","docs/screenshots/escritorio.png"],
 "AB-BI-Studio": [
    "README.md","docs/INSTALACION.md","docs/ABBI_04_oscuro.png"],
 "AB-GRAFCET-Studio-v0.1-c":["AB-GRAFCET-Studio-PORTABLE.html"],
 "AB-SCL-Studio":["AB-SCL-Studio-PORTABLE.html","docs/screenshots/scl-escritorio.png"],
 "-AB-Vision-Inspector":["AB-Vision-Inspector-PORTABLE.html"],
 "AB-KOP-Studio-v0.1":["docs/screenshots/kop-escritorio.png"]
}
RELEASES={"AB-BI-Studio":"v0.4.0","AB-Modbus-Studio":"v0.1.0"}
TOKEN=os.getenv("GITHUB_TOKEN","")
REPORT=Path("reports/PROFILE_FEATURED_LINK_QA.md")

def request(path):
    req=Request("https://api.github.com"+path,
        headers={"Accept":"application/vnd.github+json",
                 "X-GitHub-Api-Version":"2022-11-28",
                 "User-Agent":"MS-ROBOTIKA-profile-link-QA/1",
                 **({"Authorization":"Bearer "+TOKEN} if TOKEN else {})})
    with urlopen(req,timeout=25) as response:
        return json.load(response)

def main():
    readme=Path("README.md").read_text(encoding="utf-8")
    details=Path("docs/FEATURED_DEMOS.md").read_text(encoding="utf-8")
    errors=[];rows=[]
    for repo,files in REPO_FILES.items():
        for path in files:
            url=f"/repos/{OWNER}/{quote(repo,safe='')}/contents/{quote(path,safe='/')}?ref=main"
            try:
                info=request(url)
                assert info.get("type")=="file" and info.get("sha"),"Not a file"
                if path.endswith(".png"):
                    # GitHub Contents omits inline base64 for large media files.
                    # Fall back to Git Blobs by the exact SHA, never weaken PNG check.
                    content=info
                    if info.get("encoding")!="base64":
                        content=request(f"/repos/{OWNER}/{quote(repo,safe='')}/git/blobs/{info['sha']}")
                    assert content.get("encoding")=="base64","Image bytes unavailable"
                    blob=base64.b64decode(content["content"])
                    assert blob.startswith(b"\x89PNG\r\n\x1a\n") and len(blob)>=10000, "Bad PNG signature"
                rows.append((repo,path,"PASS",info.get("sha","")[:12]))
            except (HTTPError,URLError,AssertionError,KeyError,ValueError) as exc:
                errors.append((repo,path,str(exc)[:120]))
                rows.append((repo,path,"FAIL","—"))
    for repo,tag in RELEASES.items():
        name=f"{repo} release {tag}"
        try:
            release=request(f"/repos/{OWNER}/{repo}/releases/tags/{tag}")
            assert release.get("tag_name")==tag and release.get("assets"),"No release assets"
            rows.append((repo,f"release/{tag}","PASS",str(len(release["assets"]))+" assets"))
        except (HTTPError,URLError,AssertionError) as exc:
            errors.append((repo,tag,str(exc)[:120]))
            rows.append((repo,f"release/{tag}","FAIL","—"))
    for s in (
        "docs/FEATURED_DEMOS.md",
        "https://github.com/msrobotika/AB-PLC-Simulator",
        "https://github.com/msrobotika/AB-Modbus-Studio",
        "https://github.com/msrobotika/AB-BI-Studio",
        "https://raw.githubusercontent.com/msrobotika/AB-PLC-Simulator/main/docs/screenshots/lab-conveyor.png",
        "https://raw.githubusercontent.com/msrobotika/AB-Modbus-Studio/main/docs/screenshots/escritorio.png",
        "https://raw.githubusercontent.com/msrobotika/AB-BI-Studio/main/docs/ABBI_04_oscuro.png",
    ):
        if s not in readme:errors.append(("profile",s,"Not referenced in README"))
    if "github.io/AB-PLC-Simulator/" in readme:
        errors.append(("profile","Pages","Unverified GitHub Pages link"))
    if "AB-Modbus SCADA" not in details or "IN_DEVELOPMENT" not in details:
        errors.append(("docs","safety","Must clearly separate SCADA statuses"))
    if "scripts/serve.mjs" not in details or "python -m ab_modbus" not in details:
        errors.append(("docs","onboarding","Missing real first-run commands"))
    REPORT.parent.mkdir(exist_ok=True)
    lines=["# MS ROBOTIKA · Featured profile links QA","",
        "Checked UTC: "+datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "Source: GitHub REST v2022-11-28, current branch plus public main files.",
        "Only link/existence/PNG-format QA; no hardware or full-browser smoke.","",
        "| Repo | Link / asset | Result | Blob SHA / evidence |",
        "|---|---|---|---|"]
    for cells in rows:lines.append("| "+" | ".join(map(str,cells))+" |")
    lines+=["",f"**Checks:** {len(rows)}; **failures:** {len(errors)}.","",
            "## Failures"]
    lines.extend(["- "+repr(e) for e in errors] if errors else ["None."])
    REPORT.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print(f"Featured profile: {len(rows)} external checks, {len(errors)} errors")
    for e in errors:print("FAIL",repr(e))
    if errors:raise SystemExit(1)
    print("PASS: release links, downloadable HTML, screenshots (PNG signature), local run docs")

if __name__=="__main__":
    main()
