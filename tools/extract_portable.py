#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Extrae los fuentes exactos del HTML portable (operación reproducible)."""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
portable = (root / "AB-Vision-Inspector-PORTABLE.html").read_text(encoding="utf-8")
assert portable.count("<style>\n") == portable.count("\n</style>") == 1
assert portable.count("<script>\n") == portable.count("\n</script>") == 1
css = portable.split("<style>\n", 1)[1].split("\n</style>", 1)[0]
javascript = portable.split("<script>\n", 1)[1].split("\n</script>", 1)[0]
boundary = javascript.find("\n/* SPDX-License-Identifier: MIT", 30)
if boundary < 0:
    raise ValueError("No se pudo separar el motor de la interfaz")
core, app = javascript[:boundary], javascript[boundary + 1:]
if "root.ABVisionCore" not in core or "window.ABVisionCore" not in app:
    raise ValueError("Estructura inesperada del motor: extracción cancelada")
index = portable.replace("<style>\n" + css + "\n</style>",
    '<link rel="stylesheet" href="/src/style.css">')
index = index.replace("<script>\n" + javascript + "\n</script>", "")
index = index.replace(' — MS ROBOTIKA · Sin instalación</title>',
    ' — MS ROBOTIKA</title><link rel="icon" href="/favicon.svg">')
index = index.replace("</head>",
    '<script src="/src/vision-core.js" defer></script>'
    '<script src="/src/app.js" defer></script></head>')
(root / "src").mkdir(exist_ok=True)
for path, content in [
    (root / "index.html", index),
    (root / "src/style.css", css),
    (root / "src/vision-core.js", core),
    (root / "src/app.js", app),
]:
    path.write_text(content, encoding="utf-8")
    print("Verificado:", path.relative_to(root), len(content))
