# Primer recorrido · First-run guide

Revisión / Reviewed: 24/10/2026. La entrada mantenida es [AB Suite](https://github.com/msrobotika/AB-Suite-Core-arquitectura-de-integraci-n), con nueve herramientas en el mismo lanzador. / The maintained entry point is AB Suite, with nine tools in one launcher.

## Instalar · Install

[Descarga e instrucciones actuales / Current download instructions](https://github.com/msrobotika/AB-Suite-Core-arquitectura-de-integraci-n#descargar-e-instalar). En Windows, Setup y Portable incluyen los motores; el artefacto de revisión requiere sesión de GitHub y tiene conservación limitada. El instalador no tiene firma digital y todavía no se anuncia una versión estable.

Windows Setup and Portable include runtimes. The review artifact requires GitHub sign-in and has limited retention. The installer is unsigned; a stable public release is pending.

Para desarrollar desde fuentes / For source development:

```sh
git clone https://github.com/msrobotika/AB-Suite-Core-arquitectura-de-integraci-n.git
cd AB-Suite-Core-arquitectura-de-integraci-n
node scripts/setup.mjs
node scripts/workspace.mjs
```

Esta modalidad requiere Node.js 20+ y Python 3.11+. Abre la dirección local que muestra la consola. / This mode requires Node.js 20+ and Python 3.11+. Open the local address shown in the console.

## Elegir y crear · Choose and create

1. Abre AB Suite. El lanzador muestra las nueve aplicaciones. / Open AB Suite. The launcher shows all nine applications.
2. Elige cualquier herramienta y pulsa **＋ Nuevo**. / Choose any tool and select **＋ New**.
3. Crea tu proyecto; el anterior sigue disponible en **Proyectos**. Los ejemplos son opcionales. / Create your project; the previous one remains available in **Projects**. Examples are optional.

En KOP puedes eliminar la última red y empezar vacío. En Vision puedes cargar una imagen propia, elegir cámara y configurar el rango de detección. En BI puedes crear un espacio vacío o importar datos a otro espacio. / In KOP, delete the last rung to start empty. In Vision, load your image, choose a camera and set the detection range. In BI, start an empty workspace or import into a new workspace.

[Pasos por herramienta / Steps for each tool](https://github.com/msrobotika/AB-Suite-Core-arquitectura-de-integraci-n/blob/main/docs/NEW_USER_WORKFLOW.md) · [Ejercicio PLC → Modbus → BI / Connected exercise](https://github.com/msrobotika/AB-Suite-Core-arquitectura-de-integraci-n/blob/main/docs/WORKFLOW_PLC_MODBUS_BI.md)

## Capturas y alcance · Screenshots and scope

[Lanzador y nueve herramientas / Launcher and nine tools](https://github.com/msrobotika/AB-Suite-Core-arquitectura-de-integraci-n/blob/main/docs/SCREENSHOTS.md). Las imágenes de portada proceden de `docs/screenshots/suite.png`, `kop.png` y `vision.png` del repositorio integrado. Se capturaron ejecutando la aplicación con datos de laboratorio.

Screenshots show the running suite with laboratory data. The [validation record](https://github.com/msrobotika/AB-Suite-Core-arquitectura-de-integraci-n/blob/main/docs/VALIDATION.md) documents automated checks and remaining limits. Physical cameras and external hardware require separate validation; these laboratories do not certify industrial control systems.
