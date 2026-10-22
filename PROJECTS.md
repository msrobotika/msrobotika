# MS ROBOTIKA — Catálogo y auditoría de repositorios

**Revisión:** 22 de octubre de 2026 · **Alcance:** 17 repositorios del usuario `msrobotika`. Esta tabla refleja una inspección puntual de ramas `main`; algunos proyectos mantienen prototipos y trabajo experimental.

## Software industrial y productividad

| Repositorio | Área | Evidencia comprobable | Advertencia de alcance |
|---|---|---|---|
| [AB-SCL-Studio](https://github.com/msrobotika/AB-SCL-Studio) | Structured Text → Ladder | [CI aprobada](https://github.com/msrobotika/AB-SCL-Studio/actions/runs/39789383735) · [4 capturas](https://github.com/msrobotika/AB-SCL-Studio/tree/main/docs/screenshots) | Conversión booleana restringida, no compilador ST completo |
| [AB-KOP-Studio-v0.1](https://github.com/msrobotika/AB-KOP-Studio-v0.1) | Simulador KOP/Ladder | [CI aprobada](https://github.com/msrobotika/AB-KOP-Studio-v0.1/actions/runs/39784636094) · [5 capturas](https://github.com/msrobotika/AB-KOP-Studio-v0.1/tree/main/docs/screenshots) | Sin comunicación física con PLC |
| [AB-GRAFCET-Studio-v0.1-c](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c) | Editor GRAFCET v0.2 | [CI aprobada](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c/actions/runs/39725433586) · 5 capturas | **Privado**; las capturas no son accesibles públicamente hasta cambiar la visibilidad |
| [AB-Serial-Analyzer-v0.1-](https://github.com/msrobotika/AB-Serial-Analyzer-v0.1-) | Análisis RX y Modbus RTU | [CI aprobada](https://github.com/msrobotika/AB-Serial-Analyzer-v0.1-/actions/runs/39716975341) · [3 capturas](https://github.com/msrobotika/AB-Serial-Analyzer-v0.1-/tree/main/docs/screenshots) | Hardware RS-485 pendiente de validación física |
| [-AB-Vision-Inspector](https://github.com/msrobotika/-AB-Vision-Inspector) | Visión y auditoría de medidas | [CI aprobada](https://github.com/msrobotika/-AB-Vision-Inspector/actions/runs/39686572602) · [4 capturas](https://github.com/msrobotika/-AB-Vision-Inspector/tree/main/docs/screenshots) | No certificado para metrología ni seguridad |
| [AB-Modbus-Studio](https://github.com/msrobotika/AB-Modbus-Studio) | Diagnóstico Modbus | [CI aprobada](https://github.com/msrobotika/AB-Modbus-Studio/actions/runs/39669247580) · [capturas](https://github.com/msrobotika/AB-Modbus-Studio/tree/main/docs/screenshots) | No sustituye pruebas con hardware |
| [AB-BI-Studio](https://github.com/msrobotika/AB-BI-Studio) | BI y dashboards | [CI aprobada](https://github.com/msrobotika/AB-BI-Studio/actions/runs/39645487285) · [galería](https://github.com/msrobotika/AB-BI-Studio/tree/main/docs) | Ver restricciones del motor y formatos |

## Investigación, IA y aplicaciones

| Repositorio | Enfoque | Estado de evidencia / siguiente mejora |
|---|---|---|
| [AB-GEN-Green-AI](https://github.com/msrobotika/AB-GEN-Green-AI) | Visión eficiente, investigación | **Auditoría en curso:** distinguir métricas reportadas, recuperadas y reproducidas; no presentar 80,14 % como una ruta reconstruida |
| [AB-GEN-MEDICAL-DEMO.](https://github.com/msrobotika/AB-GEN-MEDICAL-DEMO.) | Demostración de IA para células sanguíneas | Investigación/prototipo: evitar afirmaciones clínicas sin validación; **sin LICENSE** en el árbol revisado |
| [AgroVive-M5-Dashboard](https://github.com/msrobotika/AgroVive-M5-Dashboard) | Demo agrícola | Métricas y consumo energético necesitan protocolo reproducible; README indica AGPL-3.0 pero **no hay LICENSE** en la raíz revisada. Revisar imágenes/datos de entrenamiento versionados y permisos |
| [Offscreen](https://github.com/msrobotika/Offscreen) | Misiones exteriores con embeddings locales | README técnicamente documentado y LICENSE; agregar gobernanza y CI apropiada para Next.js |
| [MSA-CyberDeck](https://github.com/msrobotika/MSA-CyberDeck) | Herramienta Android experimental | El README diferencia la APK 0.37 del `main` 0.1: mantener esa distinción y enlazar las validaciones de hardware |

## Dispositivos experimentales

| Repositorio | Enfoque | Mejoras prioritarias |
|---|---|---|
| [MSA-BLE-Scout](https://github.com/msrobotika/MSA-BLE-Scout) | Exploración BLE autorizada | Evidencia de firmware y capturas; plantilla para incidencias y contribución |
| [MSA-WiFi-Sentinel](https://github.com/msrobotika/MSA-WiFi-Sentinel) | Observación Wi-Fi | CI/capturas presentes; protocolo de contribuciones y límites de falsos positivos |
| [MSA-ChipSafe](https://github.com/msrobotika/MSA-ChipSafe) | Herramienta experimental para chips | Captura e instrucciones; faltan CI y política de seguridad |
| [MSA-RogueWatch](https://github.com/msrobotika/MSA-RogueWatch) | Observación pasiva Wi-Fi | **1726 archivos versionados**, incluidos muchos dentro de `firmware/.pio/build/`; se requiere limpieza del índice después de inventario y verificación de compilación |
| [msrobotika](https://github.com/msrobotika/msrobotika) | Perfil público y documentación | Esta misma portada y este inventario |

## Criterios de publicación profesional

1. **Información correcta antes que publicidad:** estado de validación visible; no presentar pruebas de laboratorio como certificados ni cifras históricas como reproducciones.
2. **Fuentes editables:** aplicación, instrucciones reproducibles, licencia apropiada, historial de cambios y control de versiones. No publicar únicamente ZIP o capturas.
3. **Pruebas objetivas:** CI declarada, comandos de reproducción, diferenciación entre test unitario, integración y ensayo físico. No se anuncia CI verde si no lo está.
4. **Capturas auténticas:** imagen generada por el programa o firmware y documentada; se identifican demos/simulaciones; sin mockups presentados como dispositivos.
5. **Seguridad:** separación clara entre observar, simular y controlar hardware; reportes de vulnerabilidad privados sin exponer instalaciones.
6. **Licencias:** un repo sin archivo de licencia no debe anunciarse automáticamente como software abierto bajo MIT/AGPL. Es necesario definir derechos de código, dependencias, modelos y datos.
7. **Limpieza y releases:** archivos compilados fuera de `git` salvo distribución intencional; paquetes en GitHub Releases, con sumas y versiones, una vez comprobados.

**Importante:** este catálogo no certifica que todas las aplicaciones estén completas o listas para producción. Los estados son los observados durante la revisión y cambian con nuevos commits.
