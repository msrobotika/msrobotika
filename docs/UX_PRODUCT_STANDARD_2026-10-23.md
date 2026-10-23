# MS ROBOTIKA — Norma de producto, UX y utilidad real
**Edición:** 2026-10-23 · **Ámbito:** todas las aplicaciones publicadas y futuras

> **Objetivo:** una persona que no haya participado en el desarrollo debe poder comprender, ejecutar y aprovechar la aplicación sin asistencia del autor. **Una interfaz bonita no constituye un producto útil.**

Esta norma es una **puerta de aceptación**; no se declara cumplida para cada repositorio por el hecho de publicar este documento. Clasificar funcionalidades como implementadas, verificadas, experimentales o pendientes con evidencias. Respetar los cambios concurrentes de otros hilos: auditar el SHA actual, aislar cambios en ramas, pasar CI, revisar PR y no sobrescribir avances.

## 1. Valor demostrable (BLOQUEANTE)

Por aplicación se documentará en `docs/UX_PRODUCT_AUDIT.md`:

- **Usuario objetivo y problema**: rol concreto (técnico de mantenimiento, programador PLC, calidad, analista, aficionado a ESP32, etc.) y tarea real que quiere resolver.
- **Tarea de valor**: entrada → acciones → resultado verificable; incluir un ejemplo de datos ficticios o simulación reproducible, sin dispositivos externos si el hardware no es imprescindible.
- **Beneficio**: qué evita o mejora respecto a hacerlo manualmente. Evitar cifras de ROI, precisión, tiempo, energía o calidad sin prueba controlada.
- **Alcance honesto**: funcionalidad real, demo, prototipo, investigación; nunca describir simuladores como controles certificados, ni datos sintéticos como mediciones de fábrica.
- **Si el usuario no logra una tarea útil**: corregir el flujo antes de añadir otro módulo.

## 2. Primera experiencia: de cero a un resultado

- Pantalla inicial con **qué es**, **qué puedo probar**, **qué necesito** y **cómo vuelvo al inicio**.
- Ruta guiada contextual de 3–5 pasos, sin tutorial interminable ni registro innecesario.
- Ejemplo precargado o importable en un clic (solo datos sintéticos/abiertos con permiso). Controles importantes visibles, avanzados en secciones colapsables cuando convenga.
- Preferir **una acción principal por pantalla**. No inundar la vista con diagnósticos, tablas ni términos internos antes de producir un resultado.
- Mostrar claramente **estado actual**, **resultado**, **por qué ha ocurrido**, **qué hacer después** y **cómo exportar/guardar**.
- Evitar falsas demos online: un archivo HTML descargable, un servidor local y una URL GitHub Pages habilitada son modalidades distintas; documentarlas con precisión.
- Métrica objetivo para ensayos con participantes externos: **primer resultado útil en ≤3 minutos** para apps de navegador, **≤5 minutos** para apps instalables, a partir de un entorno con requisitos satisfechos. Son objetivos, no datos observados.

## 3. Diseño de interfaz — sistema coherente sin clonar la identidad

- Tipografía legible y contraste suficiente. Evaluar **WCAG 2.2 AA** para texto, controles y estados; comprobar medidas de contraste, no afirmarlo por intuición.
- Componentes consistentes: espaciado, tamaños de botones, iconos acompañados de texto, jerarquía visual y nombres de acciones inequívocos.
- Verificar uso en **390, 768 y 1366 px** como mínimo, sin desplazamiento horizontal inesperado en flujos principales.
- Objetivos táctiles de al menos **44×44 CSS px** cuando sean practicables, con separación adecuada; teclado completo, foco visible, etiquetas accesibles, estados no expresados únicamente por color.
- Soportar `prefers-reduced-motion` para animaciones no esenciales; evitar redibujar innecesariamente regiones `aria-live`.
- Distinguir selectores y botones interactivos de información de solo lectura; no dejar acciones que parecen funcionar pero no tienen comportamiento real.
- Mantener idioma consistente en cada flujo (español claro; inglés como internacionalización real o documentación, no mezcla indiscriminada).
- Los gráficos requieren etiquetas de ejes, unidades, contexto de tiempo y distinción entre señal real, calculada y simulada.

## 4. Estados y recuperación

Cubrir explícitamente los estados **vacío, listo, procesando, resultado, error, desconectado, sin permisos, pausa y finalizado** cuando correspondan.

- Errores comprensibles, con causa probable y **siguiente acción**; jamás ocultar excepciones o decir solo «falló».
- Importación de ficheros: formato/tamaño permitido, validación, muestra, rechazo seguro y posibilidad de recuperar el trabajo.
- Operaciones destructivas: confirmación contextual; guardar/exportar con nombre útil y mensaje de éxito solo cuando se confirme.
- Cámara, serie, Bluetooth, Modbus o red: conexión siempre explícita y autorizada, estado visible, posibilidad de desconectar; jamás fingir datos reales en ausencia de hardware.
- Local/offline significa realmente local/offline o se explican todas las dependencias y las descargas iniciales.
- Ninguna alerta UI de un simulador sustituye enclavamientos físicos, E-STOP o seguridad funcional.

## 5. QA UX obligatoria antes de presentar el proyecto

Registrar en `docs/UX_PRODUCT_AUDIT.md` los resultados con fecha, commit, entorno, capturas y archivos de evidencia:

1. **Smoke test de primera sesión** desde checkout limpio, con ruta de usuario de principio a fin.
2. Flujo completo con ejemplo y resultado esperado reproducible.
3. Caso negativo: entrada inválida o fallo simulado y mensaje de recuperación comprobado.
4. Prueba teclado: navegación, activación de acciones y foco perceptible.
5. Responsive a 390/768/1366 px; comprobar que las acciones básicas no quedan ocultas.
6. Revisión de accesibilidad automatizada + manual; documentar hallazgos y no declarar cumplimiento total por pasar axe.
7. Pruebas de persistencia y exportación/importación de un artefacto real, si existen.
8. Limpiar bugs P0/P1; documentar P2/P3 con dueño, reproducción y prioridad.
9. Capturas de una ejecución auténtica, con etiqueta de origen y estado de desarrollo.
10. Ensayo con personas **ajenas al desarrollo** cuando sea posible: objetivo inicial 4/5 completan la tarea sin ayuda y sin incidentes graves; anotar observación real, no inventar métricas.

Si no existe navegador ni hardware en el entorno de trabajo, marcar cada comprobación como **NO VERIFICADA** y no aprobar una release de producción basándose en documentación.

## 6. Casos de valor por producto (no intercambiables)

| Proyecto | Primera tarea útil propuesta | Evidencia imprescindible |
|---|---|---|
| AB-PLC Simulator | RUN → MARCHA → ver fotocélula/contador → inyectar fallo → diagnosticar → exportar | CPU virtual, evento/resultado, sin sugerir equipo conectado |
| AB-GRAFCET Studio | Abrir secuencia de ejemplo → activar condiciones → ver transición y su explicación → exportar | Etapas y receptividades reales del motor |
| AB-KOP Studio | Montar/enlazar pulsador NO/NC y bobina → simular → guardar JSON | Estado de bobina consistente con red simulada |
| AB-SCL Studio | Importar ST admitido → mostrar KOP equivalente → rechazar sintaxis no soportada sin corromper datos | Comparación correcta y alcance restringido |
| AB-Modbus Studio | Iniciar simulador local → leer FC03 → comprender trama → exportar | Lecturas reales contra loopback, claramente no PLC físico |
| AB-Serial Analyzer | Abrir traza sintética → filtrar/decodificar CRC → exportar diagnóstico | Tramas y mensajes de error auditables |
| AB-Vision Inspector | Importar imagen demo → detectar defecto → interpretar NOK y ajustar parámetro | Imagen y salida coherentes, límites metrológicos explícitos |
| AB-BI Studio | Importar CSV → limpiar → KPI/gráfico → exportar proyecto | Cambios de datos y filtros verificables |
| Dispositivos ESP32 | Ver pantalla/firmware real o demo claramente rotulada → comprender lectura y limitaciones | Firmware comprobado por placa, permisos/red explícitos |
| AB-GEN | Ejecutar demo o verificar paquete de resultados, con estatus de evidencia | No elevar métricas históricas a validación científica |
| AB-SCADA Studio | **En desarrollo a 2026-10-23**: definir persona, caso de valor y alcance antes de anunciar una versión | No penalizar ni publicitar como producto completo prematuramente |

## 7. Priorización y decisiones

**P0:** pérdida/corrupción de datos, peligro por comunicaciones no autorizadas, claims de seguridad engañosos. **P1:** ruta principal no ejecutable, error sin recuperación, descarga rota, demo falsa. **P2:** navegación confusa, falta de guía, mobile o teclado deficientes. **P3:** pulido visual secundario.

No publicar marketing agresivo de un proyecto con P0/P1 abiertos. No se aceptan «capturas bonitas» sin funcionalidad detrás. El constructor debe entregar PRs pequeños, capturas antes/después, pruebas y estado de conformidad **CUMPLE / NO CUMPLE / NO VERIFICADO** por criterio.

## 8. Salida obligatoria por iteración

Por cada proyecto, registrar:
- última rama/commit auditado y PRs concurrentes;
- problema UX observado y por qué importa al usuario;
- cambios de código aplicados, con enlaces a commits;
- comandos de pruebas ejecutados y **resultado real**;
- evidencias en escritorio y móvil;
- P0/P1/P2 abiertos, riesgos y limitaciones;
- siguiente incremento más valioso, sin abrir un nuevo proyecto por comodidad.

**Regla central:** primero que sirva, luego que sea fácil, después que sea bonito y finalmente que se encuentre. Las cuatro dimensiones se prueban con evidencia.
