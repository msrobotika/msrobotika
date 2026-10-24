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
SUITE="AB-Suite-Core-arquitectura-de-integraci-n"
BASE=f"https://github.com/{OWNER}/{SUITE}"
TOOLS=("plc","kop","scl","grafcet","scada","modbus","serial","vision","bi")
REPO_FILES={SUITE: [
    "README.md", "desktop/README.md", "docs/NEW_USER_WORKFLOW.md",
    "docs/LOCALIZATION_AND_INSTALLATION.md", "docs/VALIDATION.md",
    "docs/SCREENSHOTS.md", "docs/WORKFLOW_PLC_MODBUS_BI.md",
    "scripts/setup.mjs", "scripts/workspace.mjs",
    *[f"apps/{tool}/README.md" for tool in TOOLS],
    *[f"docs/screenshots/{image}.png" for image in ("suite","kop","vision")],
]}
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
    for s in (
        "docs/FEATURED_DEMOS.md",
        BASE+"#descargar-e-instalar",
        *[BASE+f"/tree/main/apps/{tool}" for tool in TOOLS],
        *[f"https://raw.githubusercontent.com/{OWNER}/{SUITE}/main/docs/screenshots/{image}.png"
          for image in ("suite", "kop", "vision")],
    ):
        if s not in readme:errors.append(("profile",s,"Not referenced in README"))
    for name in ("README.md", "PROJECTS.md", "docs/FEATURED_DEMOS.md"):
        content=Path(name).read_text(encoding="utf-8")
        if re.search(r"PORTABLE\.html|/releases/tag/v0\.[14]\.0|github\.io/AB-PLC|127\.0\.0\.1|localhost",content):
            errors.append((name,"entrypoint","Obsolete or non-public installation entry"))
        if BASE not in content:
            errors.append((name,"suite","Missing maintained suite entry"))
        # All profile-relative Markdown links must resolve in this checkout.
        for target in re.findall(r"\]\(([^)]+)\)",content):
            if "://" not in target and not target.startswith("#"):
                file=target.split("#",1)[0]
                if not (Path(name).parent/file).is_file():
                    errors.append((name,target,"Broken local link"))
    if "scripts/setup.mjs" not in details or "scripts/workspace.mjs" not in details:
        errors.append(("docs","onboarding","Missing suite source commands"))
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
    print("PASS: suite entry, nine integrated tools, current PNG screenshots, install/source docs")

if __name__=="__main__":
    main()
