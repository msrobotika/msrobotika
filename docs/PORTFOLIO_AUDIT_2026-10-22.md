# Estado del portafolio · 22 octubre 2026

**Inventario:** 17 repositorios en la cuenta: 16 proyectos y el repositorio de perfil. **15 proyectos públicos; 1 privado** (AB-GRAFCET Studio). Algunos nombres contienen prefijos/sufijos de versión o guiones adicionales: no se renombrarán automáticamente porque existen enlaces externos.

| Repositorio | Visibilidad | README | LICENSE en main | Workflow | Imágenes relevantes | Prioridad |
|---|---|---|---|---|---|---|
| AB-GEN-Green-AI | Pública | Sí | **No** | Sí | Sin capturas UI | Aclarar licencias y reproducibilidad |
| AB-GEN-MEDICAL-DEMO. | Pública | Sí | **No** | No | Sin capturas UI | Demostración no clínica; ensayos/documentos |
| AgroVive-M5-Dashboard | Pública | Sí | **No** | No | Imágenes de ejemplos agrícolas, no capturas verificadas de UI | Corregir promesas y licencia |
| Offscreen | Pública | Sí | Sí | No | Fotografía de interfaz? no evidenciada | Agregar CI/capturas reproducibles |
| MSA-BLE-Scout | Pública | Sí | Sí | Sí | Capturas de framebuffer | Mantener validación de hardware |
| MSA-WiFi-Sentinel | Pública | Sí | Sí | Sí | Capturas de framebuffer | Mantener validación de hardware |
| MSA-ChipSafe | Pública | Sí | Sí | No | Vista previa de interfaz | Agregar tests y origen de captura |
| MSA-RogueWatch | Pública | Sí | Sí | No | Capturas de UI prototipo | Documentar procedencia/cobertura |
| MSA-CyberDeck | Pública | Sí | Sí | No en main | Capturas de UI | Alinear código main con versión APK etiquetada |
| AB-BI-Studio | Pública | Sí | Sí | Sí | Capturas en docs | Mantener CI y releases verificables |
| AB-Modbus-Studio | Pública | Sí | Sí | Sí | Capturas Chromium | Mantener CI y seguridad de red |
| -AB-Vision-Inspector | Pública | Sí | Sí | Sí | Capturas Chromium | Mejorar calibración metrológica |
| AB-Serial-Analyzer-v0.1- | Pública | Sí | Sí | Sí | Capturas Chromium | Validar en UART/RS-485 real |
| AB-GRAFCET-Studio-v0.1-c | **Privada** | Sí | Sí | Sí | Capturas Chromium | Hacer pública solo si el propietario decide |
| AB-KOP-Studio-v0.1 | Pública | Sí | Sí | Sí | Capturas Chromium | Validar ampliación semántica |
| AB-SCL-Studio | Pública | Sí | Sí | Sí | Capturas Chromium | Ampliar conversiones verificadas |

**Precisión:** README/LICENSE/workflow/imágenes son un inventario de archivos en `main`, no una auditoría de procedencia y eficacia de todos los programas. La presencia de una CI no significa que su último resultado sea satisfactorio. Los resultados de clasificación AB-GEN se mantienen con el nivel de evidencia expresado en su propio repositorio.

## Prioridades transversales
- Portadas coherentes, enlaces de capturas auténticas, fichas de estado, issue y PR templates.
- CI ausente en determinados repos: requiere verificar instrucciones de build antes de diseñar una acción real; no crear workflows ficticios.
- Comprobar que README y licencia no hagan afirmaciones contradictorias.
- Releases/tags y nombres: normalizar cuando el propietario confirme la política de versiones.
