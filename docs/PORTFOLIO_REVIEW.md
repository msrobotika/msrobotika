# Revisión del portafolio · Portfolio review

**24/10/2026 · 20 repositorios públicos.** Revisión de presentación, navegación, instrucciones, enlaces, procedencia de capturas y evidencia de CI. No constituye una auditoría completa de todos los motores ni una nueva validación física de los dispositivos.

**Scope:** presentation, navigation, setup instructions, links, screenshot provenance and CI evidence across 20 public repositories. This is not a complete runtime/security audit or a new hardware validation.

## Cambios publicados · Published improvements

- 18 portadas con cabeceras vectoriales originales y navegación coherente. El perfil y la portada integrada de AB Suite conservan su entrada centrada en el lanzador.
- Nueve repositorios de origen con capturas de la edición integrada, identificadas como tales, y una instalación común. Sus fichas About y Website también remiten a AB Suite.
- Resúmenes ES/EN y accesos de primer uso en los proyectos independientes. No se atribuye una interfaz bilingüe a aplicaciones que todavía no la tienen.
- ChipSafe: funciones actuales de identificación, informe JSON y SHA-256 separadas de backup/restauración previstos.
- RogueWatch: vistas de demostración diferenciadas de detección física y del firmware pendiente de reconciliar.
- Medical: requisitos externos explícitos y nombre de carpeta compatible con Windows al clonar el repositorio terminado en punto.
- AgroVive: pasos Git LFS para obtener los modelos; los punteros no equivalen a los pesos descargados.
- PLC independiente: despliegue Pages histórico convertido en operación manual con opt-in, sin intentar publicar una web inexistente en cada cambio documental. Las pruebas de motor y capturas siguen activas.
- Inventario automático actualizado de 18 a 20 repositorios. La CI se muestra por workflow y revisión; un éxito antiguo no acredita el código actual ni oculta otro fallo.

## Mapa de los 20 repositorios · Repository map

| Repositorio | Entrada mantenida y resultado de la revisión |
| --- | --- |
| [AB Suite](https://github.com/msrobotika/AB-Suite-Core-arquitectura-de-integraci-n) | Producto integrado; lanzador, nueve herramientas, instalación y galería vigentes |
| [Perfil](https://github.com/msrobotika/msrobotika) | Entrada principal a la suite, catálogo y reglas comunes de presentación |
| [PLC](https://github.com/msrobotika/AB-PLC-Simulator) | Origen conservado; edición mantenida en AB Suite; Pages manual |
| [KOP](https://github.com/msrobotika/AB-KOP-Studio-v0.1) | Origen conservado; captura y acceso a KOP integrado |
| [SCL](https://github.com/msrobotika/AB-SCL-Studio) | Origen conservado; captura y acceso a SCL integrado |
| [GRAFCET](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c) | Origen conservado; captura y acceso a GRAFCET integrado |
| [SCADA](https://github.com/msrobotika/AB-SCADA-Studio) | Origen conservado; captura y acceso al editor HMI integrado |
| [Modbus](https://github.com/msrobotika/AB-Modbus-Studio) | Origen conservado; captura y acceso a Modbus integrado |
| [Serial](https://github.com/msrobotika/AB-Serial-Analyzer-v0.1-) | Origen conservado; captura y acceso a Serial integrado |
| [Vision](https://github.com/msrobotika/-AB-Vision-Inspector) | Origen conservado; captura y acceso a Vision integrado |
| [BI](https://github.com/msrobotika/AB-BI-Studio) | Origen conservado; captura y acceso a BI integrado |
| [BLE Scout](https://github.com/msrobotika/MSA-BLE-Scout) | Controles, placa, compilación y evidencia física documentada accesibles |
| [WiFi Sentinel](https://github.com/msrobotika/MSA-WiFi-Sentinel) | Observación pasiva; entrada ES/EN, instalación y validación localizables |
| [ChipSafe](https://github.com/msrobotika/MSA-ChipSafe) | Prototipo host de lectura; portada y estado ajustados al código disponible |
| [RogueWatch](https://github.com/msrobotika/MSA-RogueWatch) | Prototipo de interfaz; pendiente consolidación del firmware |
| [CiberDeck](https://github.com/msrobotika/MSA-CyberDeck) | APK 0.37 y etiqueta de fuentes separadas del prototipo anterior de main |
| [AB-GEN](https://github.com/msrobotika/AB-GEN-Green-AI) | Navegación ES/EN; protocolos y rutas históricas preservados |
| [Medical](https://github.com/msrobotika/AB-GEN-MEDICAL-DEMO.) | Demostrador de investigación; artefactos externos y límites visibles |
| [AgroVive](https://github.com/msrobotika/AgroVive-M5-Dashboard) | Dashboard experimental; dependencias LFS documentadas |
| [Offscreen](https://github.com/msrobotika/Offscreen) | Prototipo independiente; resumen ES, ejecución y descarga inicial del modelo claros |

## Comprobación y continuidad · Verification and follow-up

Las 18 portadas publicadas se recuperaron de GitHub y se compararon con sus SHA esperados. Se comprobaron 90 destinos relativos en esas portadas y la sintaxis XML de sus 18 cabeceras originales. El inventario comprueba además los enlaces locales de las 20 portadas.

[Inventario automático con revisiones y workflows](../reports/portfolio-status.md) · [Reglas visuales y editoriales](PORTFOLIO_IDENTITY.md) · [Catálogo actual](../PROJECTS.md)

La validación de modelos, descargas LFS, cámaras y hardware no se deduce de estas comprobaciones documentales. AB-GEN aún necesita aclarar la licencia raíz; no se ha añadido una licencia sin resolver los derechos. CiberDeck conserva pendiente la convergencia entre main, etiqueta publicada y compilación limpia; no se fusionó trabajo ajeno a esta revisión. La firma y distribución estable de AB Suite siguen pendientes de sus criterios de lanzamiento.

Historical audit files and repository histories remain available. No repositories were renamed or deleted, no research results were reclassified as validated, and no social announcement or stable release was published.
