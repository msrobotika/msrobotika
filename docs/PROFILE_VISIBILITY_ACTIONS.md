# Acciones del propietario que afectan a descubrimiento y estrellas

**Fecha de referencia:** 23/10/2026. Los campos About/Topics, Bio y seis pins **NO han sido modificados automáticamente** desde esta PR. La API GitHub conectada no dispone de esa mutación. Se necesitan clics del propietario y luego comprobar el resultado.

## 1. Fijar 6 repositorios (máxima prioridad visual)

GitHub → foto de perfil → **Your profile** → sección **Pinned / Popular repositories** → **Customize your pins** → seleccionar **hasta seis** repositorios → **Save pins**.

Orden sugerido (solo si los enlaces y el estado QA se mantienen): 

1. [AB-PLC-Simulator](https://github.com/msrobotika/AB-PLC-Simulator) — CPU virtual y fallo de línea
2. [AB-Modbus-Studio](https://github.com/msrobotika/AB-Modbus-Studio) — FC01–04 y laboratorio TCP
3. [AB-BI-Studio](https://github.com/msrobotika/AB-BI-Studio) — CSV/Excel → modelo/dashboard local
4. [-AB-Vision-Inspector](https://github.com/msrobotika/-AB-Vision-Inspector) — inspección de imagen experimental
5. [AB-GRAFCET-Studio-v0.1-c](https://github.com/msrobotika/AB-GRAFCET-Studio-v0.1-c) — secuencias SFC
6. [AB-SCL-Studio](https://github.com/msrobotika/AB-SCL-Studio) — conversión del subconjunto booleano a KOP

**No marcar la tarea como REALIZADA** antes de reabrir https://github.com/msrobotika sin sesión y comprobar que aparecen los seis. No fijar AB-SCADA Studio como terminado mientras siga IN_DEVELOPMENT.

## 2. Poner Topics reales en los tres proyectos principales

GitHub → repositorio → esquina derecha **About** → engranaje → **Topics** → pega de 5 a 7 términos, elige los resultados sugeridos cuando correspondan → **Save changes**.

| Proyecto | Topics listos para pegar (separados por espacio) |
| --- | --- |
| AB-PLC-Simulator | plc plc-simulator industrial-automation ladder-logic javascript simulation |
| AB-Modbus-Studio | modbus modbus-tcp industrial-automation python protocol-analyzer scada |
| AB-BI-Studio | business-intelligence data-visualization dashboard python data-cleaning fastapi |
| -AB-Vision-Inspector | computer-vision image-processing quality-control defect-detection metrology javascript |
| AB-GRAFCET-Studio-v0.1-c | grafcet sfc plc industrial-automation javascript simulation |
| AB-SCL-Studio | structured-text ladder-logic plc javascript industrial-automation |

El Topic **scada** de Modbus se refiere exclusivamente al **módulo de código fuente alfa**, no a la v0.1.0 publicada. No introducir Topics de fabricantes o protocolos todavía no implementados.

Tras guardar, comprueba que los Topics aparecen justo debajo de About. Revisa que la descripción en About sea específica y no anuncie firmware, compatibilidad o hardware no ensayados. No configurar el campo **Website** para el PLC: su URL de GitHub Pages devolvió HTTP 404 el día de referencia. Un enlace de README no prueba despliegue.

## 3. Propuesta de Bio corta

En GitHub → avatar → **Your profile** → **Edit profile**, introduce como propuesta de Bio (sin claims absolutos):

> MS ROBOTIKA · Open-source PLC simulation, Modbus diagnostics, industrial data & vision labs. Reproducible demos · La Rioja, Spain.

Revisa y guarda manualmente; no se ha modificado tu perfil por esta PR. El enlace Website personal se deja sin inventar una landing si no existe una página útil operativa.

## 4. Primeras estrellas: ganarlas con una prueba clara

Publicar solo después de revisar las capturas y QA de cada producto. Es mejor demostrar **una** funcionalidad concreta y pedir feedback sobre un fallo real que publicar el catálogo entero cada día.

- PLC: CPU RUN, marcha de cinta, atasco virtual, parada/diagnóstico, enlace al escenario reproducible.
- Modbus: lectura FC03 de registro 230 y trazas TX/RX, aviso de que el release antiguo NO incluye SCADA.
- BI: ZIP oficial + importación CSV de cuatro filas + primer informe, recordando que requiere Python.
- Vision: imagen patrón/defecto OK-NOK, documentando validación de escala y cámara pendiente.

Publicar ES y EN en momentos diferentes solo cuando la audiencia lo justifique. Respetar las normas anti-autopromoción de cada comunidad. No enviar posts automáticamente. Terminar con una petición útil: «¿Qué caso de fallo o límite de protocolo debería añadir al laboratorio?» y una invitación voluntaria a dejar ⭐ en el repositorio probado.

## 5. Medición, no deseos

Línea base 23/10/2026: 20 repos públicos, 14 estrellas sumadas y 0 forks, según auditoría API. Esto **no representa visitas ni personas únicas**. Registrar por repositorio Insights → Traffic (ventana de 14 días), downloads de Releases, issues externas y PRs de terceros, distinguiendo NO_DISPONIBLE. [Informe y fuentes pendientes de revisión](https://github.com/msrobotika/msrobotika/pull/2).

Registrar el antes/después solo tras ver Topics y pins aplicados; no atribuir estrellas o visitas al perfil sin datos temporales.

Documentación oficial: [Pinning items](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile), [Repository Topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics).
