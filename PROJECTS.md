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
| [AB-GEN-MEDICAL-DEMO.](https://github.com/msrobotika/AB-GEN-MEDICAL-DEMO.) | Demostración de IA para células sanguíneas | Investigación/prototipo: evitar afirmaciones clínicas sin validación; [LICENSE MIT](https://github.com/msrobotika/AB-GEN-MEDICAL-DEMO./blob/main/LICENSE) incorporada; sin validación clínica independiente |
| [AgroVive-M5-Dashboard](https://github.com/msrobotika/AgroVive-M5-Dashboard) | Demo agrícola | Métricas y consumo energético necesitan protocolo reproducible; [LICENSE AGPL-3.0](https://github.com/msrobotika/AgroVive-M5-Dashboard/blob/main/LICENSE) incorporada; métricas históricas no validadas. Revisar derechos de datos y modelos |
| [Offscreen](https://github.com/msrobotika/Offscreen) | Misiones exteriores con embeddings locales | [CI unitaria](https://github.com/msrobotika/Offscreen/actions/runs/39811701040) aprobada; la compilación/despliegue no están cubiertos por esa CI |
| [MSA-CyberDeck](https://github.com/msrobotika/MSA-CyberDeck) | Herramienta Android experimental | El README diferencia APK 0.37 de `main` 0.1; [CI estática aprobada](https://github.com/msrobotika/MSA-CyberDeck/actions/runs/39811788438), sin ensamblaje de APK |

## Dispositivos experimentales

| Repositorio | Enfoque | Mejoras prioritarias |
|---|---|---|
| [MSA-BLE-Scout](https://github.com/msrobotika/MSA-BLE-Scout) | Exploración BLE autorizada | Evidencia de firmware y capturas; plantilla para incidencias y contribución |
| [MSA-WiFi-Sentinel](https://github.com/msrobotika/MSA-WiFi-Sentinel) | Observación Wi-Fi | CI/capturas presentes; protocolo de contribuciones y límites de falsos positivos |
| [MSA-ChipSafe](https://github.com/msrobotika/MSA-ChipSafe) | Herramienta experimental para chips | Captura y [CI estática](https://github.com/msrobotika/MSA-ChipSafe/actions/runs/39811780585) aprobada; falta verificación física |
| [MSA-RogueWatch](https://github.com/msrobotika/MSA-RogueWatch) | Observación pasiva Wi-Fi | **Limpieza realizada:** retirados 1696 archivos generados (≈135 MB) de la rama principal, conservando su historial y fuentes; [CI de limpieza aprobada](https://github.com/msrobotika/MSA-RogueWatch/actions/runs/39811791527). Firmware físico pendiente |
| [msrobotika](https://github.com/msrobotika/msrobotika) | Perfil público y documentación | Esta misma portada y este inventario |


## Mejoras de gobernanza aplicadas

- Los **17 repositorios** tienen plantilla de pull request para obligar a documentar reproducción, evidencias, riesgos y resultados pendientes.
- Todos disponen ya de `CONTRIBUTING.md` y `SECURITY.md`, salvo las políticas preexistentes, que se han conservado.
- Los repositorios **Offscreen, Medical Demo, AgroVive, ChipSafe, RogueWatch y CyberDeck** incorporan verificaciones CI con alcances explícitos, aprobadas el 22 de octubre de 2026.
- La edición publicada de RogueWatch ya no versiona su carpeta de compilación `firmware/.pio`; los archivos siguen recuperables por historial Git.
- Los resultados científicos o médicos no se presentan como validados sin un protocolo repetible.

## Criterios de publicación profesional

1. **Información correcta antes que publicidad:** estado de validación visible; no presentar pruebas de laboratorio como certificados ni cifras históricas como reproducciones.
2. **Fuentes editables:** aplicación, instrucciones reproducibles, licencia apropiada, historial de cambios y control de versiones. No publicar únicamente ZIP o capturas.
3. **Pruebas objetivas:** CI declarada, comandos de reproducción, diferenciación entre test unitario, integración y ensayo físico. No se anuncia CI verde si no lo está.
4. **Capturas auténticas:** imagen generada por el programa o firmware y documentada; se identifican demos/simulaciones; sin mockups presentados como dispositivos.
5. **Seguridad:** separación clara entre observar, simular y controlar hardware; reportes de vulnerabilidad privados sin exponer instalaciones.
6. **Licencias:** un repo sin archivo de licencia no debe anunciarse automáticamente como software abierto bajo MIT/AGPL. Es necesario definir derechos de código, dependencias, modelos y datos.
7. **Limpieza y releases:** archivos compilados fuera de `git` salvo distribución intencional; paquetes en GitHub Releases, con sumas y versiones, una vez comprobados.

**Importante:** este catálogo no certifica que todas las aplicaciones estén completas o listas para producción. Los estados son los observados durante la revisión y cambian con nuevos commits.
