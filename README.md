# MS ROBOTIKA

**Software libre para automatización industrial, instrumentación, datos e inteligencia artificial local.**

**Open-source tools for PLC simulation, industrial automation, data analysis, Modbus diagnostics and local computer vision.** Research prototypes and laboratory simulators are clearly distinguished from hardware-validated systems.

## Empieza aquí · Start here

| Quiero… / I want to… | Proyecto | Primera prueba / First step |
|---|---|---|
| **Simular un PLC y una línea virtual** / simulate a PLC | [AB-PLC Simulator](https://github.com/msrobotika/AB-PLC-Simulator) | [Ejemplo reproducible: 150 ciclos y atasco simulado](https://github.com/msrobotika/AB-PLC-Simulator/blob/main/examples/conveyor-with-fault.json) · Node.js 20+ · ejecución local; **sin demo Pages activa** |
| **Aprender GRAFCET sin instalar software** / try SFC | [AB-GRAFCET Studio](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c) | [HTML portátil](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c/blob/main/AB-GRAFCET-Studio-PORTABLE.html) · descargar y abrir localmente |
| **Convertir un subconjunto SCL/ST a KOP** / try ST-to-Ladder | [AB-SCL Studio](https://github.com/msrobotika/AB-SCL-Studio) | [HTML portátil](https://github.com/msrobotika/AB-SCL-Studio/blob/main/AB-SCL-Studio-PORTABLE.html) · no es compilador PLC |
| **Probar inspección de imágenes** / try vision inspection | [AB-Vision Inspector](https://github.com/msrobotika/-AB-Vision-Inspector) | [HTML portátil](https://github.com/msrobotika/-AB-Vision-Inspector/blob/main/AB-Vision-Inspector-PORTABLE.html) · demo de laboratorio |
| **Preparar datos y gráficos** / explore local BI | [AB-BI Studio](https://github.com/msrobotika/AB-BI-Studio) | [Descarga v0.4](https://github.com/msrobotika/AB-BI-Studio/releases/tag/v0.4.0) · requiere Python |
| **Leer registros Modbus TCP** / inspect Modbus | [AB-Modbus Studio](https://github.com/msrobotika/AB-Modbus-Studio) | [Descarga v0.1](https://github.com/msrobotika/AB-Modbus-Studio/releases/tag/v0.1.0) · cliente de solo lectura |

### Tres proyectos para empezar · Three tested entry points

| Simulación PLC · PLC simulation | Diagnóstico TCP · Modbus read-only | Análisis de datos · Local BI |
| :---: | :---: | :---: |
| [![AB-PLC Simulator: transportador y CPU virtual capturados en Chromium](https://raw.githubusercontent.com/msrobotika/AB-PLC-Simulator/main/docs/screenshots/lab-conveyor.png)](https://github.com/msrobotika/AB-PLC-Simulator) | [![AB-Modbus Studio: lectura FC03 real de simulador local en Chromium](https://raw.githubusercontent.com/msrobotika/AB-Modbus-Studio/main/docs/screenshots/escritorio.png)](https://github.com/msrobotika/AB-Modbus-Studio) | [![AB-BI Studio v0.4: informe con datos de demostración](https://raw.githubusercontent.com/msrobotika/AB-BI-Studio/main/docs/ABBI_04_oscuro.png)](https://github.com/msrobotika/AB-BI-Studio) |
| **[Ejecutar PLC / Run locally](https://github.com/msrobotika/AB-PLC-Simulator#ejecutar-en-windows-linux-o-macos)** · Node.js ≥20, CPU y transportador virtual | **[Probar FC03 / Try local FC03](https://github.com/msrobotika/AB-Modbus-Studio#primera-prueba-en-menos-de-un-minuto)** · Python ≥3.11, simulador TCP | **[Instalar y abrir / Install locally](https://github.com/msrobotika/AB-BI-Studio/blob/main/docs/INSTALACION.md)** · [ZIP oficial v0.4.0](https://github.com/msrobotika/AB-BI-Studio/releases/tag/v0.4.0), requiere Python ≥3.11 |

<sub>Capturas originales guardadas en los repositorios, realizadas en navegador/laboratorio o con datos sintéticos. / Real screenshots from the projects; laboratory or synthetic data, **not physical industrial systems**. La captura de BI no es una medida de fábrica. [Evidencia y pasos reproducibles / Verification details](docs/FEATURED_DEMOS.md).</sub>

**La prueba más interesante / The connected demo:** [AB-PLC Simulator](https://github.com/msrobotika/AB-PLC-Simulator) → Modbus TCP **FC01/FC03** → [AB-Modbus Studio](https://github.com/msrobotika/AB-Modbus-Studio). La coincidencia de señales sobre **una única CPU virtual** y un atasco simulado se ha [probado con los dos programas reales en CI](https://github.com/msrobotika/AB-Modbus-Studio/actions/runs/39987456005). La integración integral PLC → Suite Core → SCADA → BI continúa en validación: **no es una planta conectada**.

**Distribución honesta / Release status:** el [ZIP v0.1.0 de Modbus](https://github.com/msrobotika/AB-Modbus-Studio/releases/tag/v0.1.0) ejecuta el cliente de laboratorio, **pero todavía no incorpora AB-Modbus SCADA**. El módulo SCADA está en código fuente y dispone de [candidatas de QA](https://github.com/msrobotika/AB-Modbus-Studio/pull/1), no de una nueva Release pública. [AB-SCADA Studio](https://github.com/msrobotika/AB-SCADA-Studio) permanece **EN DESARROLLO / IN DEVELOPMENT**, no es un producto industrial terminado.

**⭐ ¿Te ha resultado útil? / Was a tool useful?** Deja una estrella **en el repositorio de esa herramienta**, y si puedes, comparte un caso de prueba reproducible o una incidencia. / **Star the specific project** you tried and tell us what worked or what needs improving. [Cómo contribuir / Contributing](CONTRIBUTING.md) · [Primeras pruebas / First-run evidence](docs/FEATURED_DEMOS.md).



Diseñamos herramientas para analizar, simular y comprender sistemas técnicos sin depender de licencias comerciales. Cada proyecto tiene su propio repositorio, código fuente e indicaciones de uso. Indicamos de forma expresa qué está **verificado**, qué es una **demostración** y qué necesita pruebas en equipos reales.

**[Software industrial](#software-industrial)** · **[Hardware y seguridad](#hardware-y-seguridad)** · **[IA e investigación](#inteligencia-artificial-e-investigación)** · **[Política de calidad](docs/REPO_STANDARD.md)** · **[Auditoría del portafolio](docs/PORTFOLIO_AUDIT_2026-10-23.md)** · **[Estado automático](reports/portfolio-status.md)**

---

## Software industrial

| Proyecto | Para qué sirve | Estado / evidencias |
|---|---|---|
| [AB-SCL Studio](https://github.com/msrobotika/AB-SCL-Studio) | Analizador ST/SCL y conversor del subconjunto booleano compatible a KOP | v0.1 · pruebas y 4 capturas |
| [AB-PLC Simulator](https://github.com/msrobotika/AB-PLC-Simulator) | Laboratorio de CPU PLC virtual, bastidor E/S y procesos simulados; admite proyectos AB-KOP compatibles | v0.4 de laboratorio · CI, pruebas y capturas |
| [AB-KOP Studio](https://github.com/msrobotika/AB-KOP-Studio-v0.1) | Editor y simulador Ladder, contactos, bobinas y TON por ciclos | v0.1 · pruebas y 5 capturas |
| [AB-GRAFCET Studio](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c) | Editor y simulador de etapas, receptividades y diagnóstico | v0.2 · repositorio público; pruebas y 5 capturas |
| [AB-Serial Analyzer](https://github.com/msrobotika/AB-Serial-Analyzer-v0.1-) | Diagnóstico serie y Modbus RTU, CRC, monitor y laboratorio local | v0.1 · pruebas y 3 capturas |
| [AB-Modbus Studio](https://github.com/msrobotika/AB-Modbus-Studio) | Cliente Modbus TCP de lectura, simulador y monitor | v0.1 · pruebas y 3 capturas |
| [AB-Vision Inspector](https://github.com/msrobotika/-AB-Vision-Inspector) | Inspección visual y metrología experimental con auditoría de cámara | v0.3 alfa · pruebas y 4 capturas |
| [AB-BI Studio](https://github.com/msrobotika/AB-BI-Studio) | Visualización, modelo semántico y análisis de datos | v0.4 · aplicación con capturas y CI |

<table>
  <tr>
    <td width="50%"><a href="https://github.com/msrobotika/AB-SCL-Studio"><img src="https://raw.githubusercontent.com/msrobotika/AB-SCL-Studio/main/docs/screenshots/scl-escritorio.png" alt="AB-SCL Studio: editor real con conversión KOP" width="100%"></a><br><sub>AB-SCL Studio · aplicación en Chromium</sub></td>
    <td width="50%"><a href="https://github.com/msrobotika/AB-KOP-Studio-v0.1"><img src="https://raw.githubusercontent.com/msrobotika/AB-KOP-Studio-v0.1/main/docs/screenshots/kop-escritorio.png" alt="AB-KOP Studio: monitor Ladder real" width="100%"></a><br><sub>AB-KOP Studio · lógica Ladder simulada</sub></td>
  </tr>
</table>

Las salidas y mediciones de estas aplicaciones no equivalen a certificación ni a control industrial seguro. La validación en PLC y hardware físico se documentará por separado.

## Hardware y seguridad

| Proyecto | Función principal | Estado declarado |
|---|---|---|
| [MSA BLE Scout](https://github.com/msrobotika/MSA-BLE-Scout) | Inspector portátil Bluetooth LE de lectura y evidencias | Prototipo experimental, capturas de framebuffer |
| [MSA WiFi Sentinel](https://github.com/msrobotika/MSA-WiFi-Sentinel) | Observación pasiva Wi-Fi 2,4 GHz en ESP32 | Prueba física descrita, capturas del dispositivo |
| [MSA ChipSafe](https://github.com/msrobotika/MSA-ChipSafe) | Auditoría e integridad de firmware de placas propias | Prototipo inicial |
| [MSA RogueWatch](https://github.com/msrobotika/MSA-RogueWatch) | Observación de redes autorizadas y alertas indicativas | Prototipo, interfaz de demostración |
| [MSA CyberDeck](https://github.com/msrobotika/MSA-CyberDeck) | Herramientas Android de inspección y documentación | APK de desarrollo; `main` no corresponde necesariamente a la última APK |

Estas herramientas están destinadas a equipos propios o autorizados; las alertas observadas no prueban automáticamente una intrusión.

## Inteligencia artificial e investigación

| Proyecto | Objetivo | Estado y límites |
|---|---|---|
| [AB-GEN Green AI](https://github.com/msrobotika/AB-GEN-Green-AI) | Arquitectura experimental de clasificación visual eficiente | **Auditoría de reproducibilidad abierta**: resultados históricos no se consideran validados |
| [AB-GEN Medical Demo](https://github.com/msrobotika/AB-GEN-MEDICAL-DEMO.) | Demostración de clasificación y explicabilidad sobre imágenes hematológicas | **No es diagnóstico clínico**, no validado para pacientes |
| [AgroVive M5 Dashboard](https://github.com/msrobotika/AgroVive-M5-Dashboard) | Exploración de visión artificial agrícola | Cifras históricas de rendimiento/energía pendientes de verificación independiente |
| [Offscreen](https://github.com/msrobotika/Offscreen) | Experiencias al aire libre sugeridas mediante embeddings locales en navegador | Prototipo web; descarga inicial de modelo y runtime |

---

## Cómo evaluamos cada proyecto

**Código comprobable.** README con instrucciones claras y enlaces a sus fuentes. Las pruebas y CI se anuncian solo cuando existen y han sido ejecutadas; no se confunde una insignia con evidencia.

**Capturas auténticas.** Se enlazan fotografías, framebuffer o pantallas ejecutadas realmente, etiquetadas según su procedencia. Una maqueta se identifica como tal. Los proyectos sin capturas quedan explícitamente pendientes.

**Licencias claras.** Solo se declara software libre con un archivo de licencia y titularidad apropiada. Algunas investigaciones antiguas requieren aclarar la licencia antes de redistribuirse.

**Seguridad y alcance.** Los simuladores no programan PLC físicos ni sustituyen sistemas de seguridad. Los clasificadores agrícolas/médicos experimentales no deben utilizarse para decisiones de alto riesgo sin validación.

**Contribuciones.** Las incidencias, propuestas y pull requests están abiertas en cada repositorio según sus permisos. Consulta el [estándar de mantenimiento](docs/REPO_STANDARD.md) y la [auditoría por proyecto](docs/PORTFOLIO_AUDIT_2026-10-23.md).

<sub>© 2026 MS ROBOTIKA · Portafolio mantenido por proyecto · última revisión documental: 23 de octubre de 2026.</sub>
