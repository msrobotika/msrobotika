#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Extrae los componentes originales del portable, preservando el código exacto."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
portable = (ROOT / "AB-Vision-Inspector-PORTABLE.html").read_text(encoding="utf-8")
assert portable.count("<style>") == portable.count("</style>") == 1
assert portable.count("<script>") == portable.count("</script>") == 1
style = portable.split("<style>", 1)[1].split("</style>", 1)[0]
javascript = portable.split("<script>", 1)[1].split("</script>", 1)[0]
boundary = javascript.find("/* SPDX-License-Identifier: MIT", 3)
if boundary <= 0 or "window.ABVisionCore" not in javascript:
    raise ValueError("No se reconoce el formato del portable: abortar extracción.")
core, app = javascript[:boundary], javascript[boundary:]
assert "window.ABVisionCore" in core and "ABVisionCore" in app
ROOT.joinpath("src").mkdir(exist_ok=True)
(ROOT / "src" / "style.css").write_text(style, encoding="utf-8")
(ROOT / "src" / "vision-core.js").write_text(core, encoding="utf-8")
(ROOT / "src" / "app.js").write_text(app, encoding="utf-8")
html = portable.replace("<style>" + style + "</style>",
                        '<link rel="stylesheet" href="src/style.css">')
html = html.replace("<script>" + javascript + "</script>",
                    '<script src="src/vision-core.js" defer></script>'
                    '<script src="src/app.js" defer></script>')
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("Extraídos index.html, estilos, motor de visión y aplicación JS")
