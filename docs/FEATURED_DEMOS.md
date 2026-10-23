# Primera prueba · First-run evidence

**MS ROBOTIKA · 23/10/2026.** Laboratorios de software, sin conexión a máquinas. Las pruebas no acreditan seguridad funcional, certificación industrial ni compatibilidad total con PLC físicos.

**English:** Three reproducible local lab workflows, original screenshots, exact GitHub Actions evidence, and clearly stated limits. Star the specific tool that is useful—not the whole catalogue automatically.

## 1. AB-PLC Simulator · CPU virtual y atasco de transportador

Requisitos: Node.js 20+ y Git. / Requirements: Node.js 20+ and Git.

    git clone https://github.com/msrobotika/AB-PLC-Simulator.git
    cd AB-PLC-Simulator
    node scripts/serve.mjs

Abre http://127.0.0.1:4173/ para iniciar CPU RUN y marcha. Ensayo reproducible sin navegador:

    node scripts/run-scenario.mjs --scenario examples/conveyor-with-fault.json --csv conveyor-demo.csv

Incluye 150 scans, inyección de atasco y recuperación virtual. Captura [transportador real en Chromium](https://github.com/msrobotika/AB-PLC-Simulator/blob/main/docs/screenshots/lab-conveyor.png). Evidencia: [CI de instalación limpia, Linux/Windows/macOS](https://github.com/msrobotika/AB-PLC-Simulator/actions/runs/39983164360), caso de cinta y depósito, controles de acceso HTTP.

**No hay demo pública Pages verificada:** la URL de GitHub Pages respondió HTTP 404 el 23/10/2026. Se requiere ejecución local. [Repositorio / ⭐ Star](https://github.com/msrobotika/AB-PLC-Simulator).

## 2. AB-Modbus Studio · FC03 real contra simulador local

Requisitos: Python 3.11+; no se conecta a un PLC físico. / Python 3.11+, localhost only.

    git clone https://github.com/msrobotika/AB-Modbus-Studio.git
    cd AB-Modbus-Studio
    python -m ab_modbus --self-test
    python -m ab_modbus

Desde la HMI pulsa Iniciar y probar FC03; lee ocho registros sintéticos, empezando por 230, 1500, 42 y 2026. [Captura auténtica del laboratorio](https://github.com/msrobotika/AB-Modbus-Studio/blob/main/docs/screenshots/escritorio.png).

**Suite verificada:** [CI de interoperabilidad PLC ↔ Modbus](https://github.com/msrobotika/AB-Modbus-Studio/actions/runs/39987456005) arrancó AB-PLC Simulator y comparó las salidas y scan de la misma CPU virtual con lecturas FC01/FC03 del cliente real. Inyectó un atasco virtual; no hubo comandos a maquinaria.

**Atención al descargar:** la [Release v0.1.0](https://github.com/msrobotika/AB-Modbus-Studio/releases/tag/v0.1.0) funciona como cliente FC01–04 en Windows/Linux pero **sus ZIP no incorporan AB-Modbus SCADA**. El módulo de supervisión está en el código fuente y en [candidatas de QA](https://github.com/msrobotika/AB-Modbus-Studio/pull/1), no en una Release nueva. [Seguimiento](https://github.com/msrobotika/AB-Modbus-Studio/issues/2) · [Repositorio / ⭐ Star](https://github.com/msrobotika/AB-Modbus-Studio).

## 3. AB-BI Studio · CSV a modelo de datos

Requisitos: Python 3.11+ e Internet para instalar dependencias. Descarga [ZIP oficial v0.4.0 y SHA-256](https://github.com/msrobotika/AB-BI-Studio/releases/tag/v0.4.0), extrae el ZIP completo y ejecuta iniciar.bat (Windows) o iniciar.sh (Linux).

Importa examples/datos_para_limpiar.csv y examina las cuatro filas. La [CI de la Release oficial](https://github.com/msrobotika/AB-BI-Studio/actions/runs/39988774312) verificó en Windows y Ubuntu el hash, el manifiesto, instalación en un venv limpio, HMI y carga real de las cuatro filas. No probó el doble clic en el PC de un usuario. **Es un ZIP de fuentes con lanzadores, NO un EXE autónomo ni un clon completo de Power BI.**

[Captura de informe de demostración](https://github.com/msrobotika/AB-BI-Studio/blob/main/docs/ABBI_04_oscuro.png) · [Guía de instalación](https://github.com/msrobotika/AB-BI-Studio/blob/main/docs/INSTALACION.md) · [Repositorio / ⭐ Star](https://github.com/msrobotika/AB-BI-Studio).

## 4. Conjunto MS ROBOTIKA y límites

AB-PLC Simulator simula la CPU; AB-Modbus Studio inspecciona registros; AB-Suite Core transporta eventos; AB-SCADA Studio supervisa; AB-BI Studio prepara y analiza datos.

**Probado como recorrido entre dos productos:** PLC virtual ↔ Modbus Studio. Las pruebas de Core y SCADA/BI por separado NO demuestran todavía el recorrido conjunto PLC → SCADA → BI en una sola sesión. [AB-SCADA Studio](https://github.com/msrobotika/AB-SCADA-Studio) permanece **IN_DEVELOPMENT / EN DESARROLLO** y no debe confundirse con el módulo AB-Modbus SCADA.

## 5. Apoyo y métricas sin engaños

Una ⭐ ayuda cuando nace de una experiencia real. Lo más útil después de probar el software es [informar de un fallo reproducible o contribuir](../CONTRIBUTING.md). Se registran stars por repo, no seguidores falsos. Visitantes únicos, clones y referidos necesitan datos reales de GitHub Insights; no se deducen de las estrellas.

English: **try a real local demo, inspect the linked test run, and star only the repository that helped you.** Reproducible issues and independent contributions are especially welcome.
