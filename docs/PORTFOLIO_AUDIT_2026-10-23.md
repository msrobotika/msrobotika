# Auditoría documental del portafolio · 23 octubre 2026

**Alcance:** 18 repositorios públicos de GitHub, que incluyen 17 proyectos y el repositorio de perfil `msrobotika`. Se revisaron los árboles de la rama predeterminada y los enlaces internos de los README. Esta auditoría **no** equivale a ejecutar o certificar 17 aplicaciones.

**Resultado del control documental:** 17 README de proyecto examinados sin referencias locales ausentes detectadas por el comprobador Markdown/HTML básico. Todos incluyen `docs/PROJECT_STATUS.md`. El [informe generado automáticamente](../reports/portfolio-status.md) registra variaciones futuras y la última ejecución de CI que devuelva GitHub.

| Proyecto | Público | README | LICENSE | CI definida | Recursos visuales |
|---|:---:|:---:|:---:|:---:|:---:|
| [AB-GEN Green AI](https://github.com/msrobotika/AB-GEN-Green-AI) | Sí | Sí | **No** | Sí | No verificados |
| [AB-GEN Medical Demo](https://github.com/msrobotika/AB-GEN-MEDICAL-DEMO.) | Sí | Sí | Sí | Sí | Sin capturas UI en rama principal |
| [AgroVive M5](https://github.com/msrobotika/AgroVive-M5-Dashboard) | Sí | Sí | Sí | Sí | Imágenes agrícolas, no capturas del software |
| [Offscreen](https://github.com/msrobotika/Offscreen) | Sí | Sí | Sí | Sí | Fotografía de apoyo, no captura de funcionamiento |
| [MSA BLE Scout](https://github.com/msrobotika/MSA-BLE-Scout) | Sí | Sí | Sí | Sí | Capturas de framebuffer |
| [MSA WiFi Sentinel](https://github.com/msrobotika/MSA-WiFi-Sentinel) | Sí | Sí | Sí | Sí | Capturas de framebuffer |
| [MSA ChipSafe](https://github.com/msrobotika/MSA-ChipSafe) | Sí | Sí | Sí | Sí | Vista de interfaz; requiere distinguir render/prototipo |
| [MSA RogueWatch](https://github.com/msrobotika/MSA-RogueWatch) | Sí | Sí | Sí | Sí | Capturas de UI de prototipo |
| [MSA CyberDeck](https://github.com/msrobotika/MSA-CyberDeck) | Sí | Sí | Sí | Sí | Capturas de aplicación; diferenciar APK y rama main |
| [AB-BI Studio](https://github.com/msrobotika/AB-BI-Studio) | Sí | Sí | Sí | Sí | Capturas dashboard |
| [AB-Modbus Studio](https://github.com/msrobotika/AB-Modbus-Studio) | Sí | Sí | Sí | Sí | Capturas de Chromium |
| [AB-Vision Inspector](https://github.com/msrobotika/-AB-Vision-Inspector) | Sí | Sí | Sí | Sí | Capturas de Chromium |
| [AB-Serial Analyzer](https://github.com/msrobotika/AB-Serial-Analyzer-v0.1-) | Sí | Sí | Sí | Sí | Capturas de Chromium |
| [AB-GRAFCET Studio](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c) | Sí | Sí | Sí | Sí | Capturas de Chromium |
| [AB-KOP Studio](https://github.com/msrobotika/AB-KOP-Studio-v0.1) | Sí | Sí | Sí | Sí | Capturas de Chromium |
| [AB-SCL Studio](https://github.com/msrobotika/AB-SCL-Studio) | Sí | Sí | Sí | Sí | Capturas de Chromium |
| [AB-PLC Simulator](https://github.com/msrobotika/AB-PLC-Simulator) | Sí | Sí | Sí | Sí | Capturas de laboratorio virtual |

El repositorio [msrobotika/msrobotika](https://github.com/msrobotika/msrobotika) es el número **18**: contiene la portada, la política común y la auditoría automatizada. Los proyectos industriales no se consideran aptos para control o seguridad de máquinas por contar con CI.

## Prioridades de trabajo verificables

1. **AB-GEN:** aclarar derechos y licencia antes de atribuir condiciones de redistribución. No publicar métricas históricas como reproducción validada; revisar fugas de datos y semántica de inferencia.
2. **AB-GEN Medical y AgroVive:** mantener avisos de carácter demostrativo y separar evaluaciones en datasets de las validaciones sobre casos reales.
3. **Industrial:** documentar escenarios de prueba sobre hardware y diferencias entre simuladores, PLC y comunicaciones físicas.
4. **Ciberseguridad ESP32:** preservar evidencia de pantalla física frente a renders; pruebas por modelo y permisos de red autorizada.
5. **Catálogo:** normalizar versiones mediante etiquetas/releases sin romper nombres o enlaces existentes; evitar renombrado automático.

## Qué verifica realmente el control

- Existencia documental: README, LICENSE, SECURITY, ficha de estado, workflows y recursos visuales.
- Vínculos relativos sencillos de Markdown/HTML dentro de README.
- Resultado de la última CI *completada* disponible, no necesariamente del último commit.
- No inspecciona secretos, no revisa licencias de terceros, no prueba metrología ni veracidad de modelos.

Para un inventario actualizado de forma recurrente: [reports/portfolio-status.md](../reports/portfolio-status.md).
Se mantiene la [auditoría anterior (22 oct)](PORTFOLIO_AUDIT_2026-10-22.md) por trazabilidad.
