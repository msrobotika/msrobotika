# MS ROBOTIKA · Estándar de repositorios

Aplicable al código actual y a las futuras publicaciones. Se distingue entre **objetivo** y **requisito ya cumplido**; no todos los proyectos están en el mismo nivel de madurez.

## Portada y documentación
- README en el idioma de los usuarios, con objetivo, versión, requisitos, instalación, ejemplo reproducible y límites.
- Licencia en la raíz solo cuando los derechos de distribución estén claros.
- `docs/PROJECT_STATUS.md` para mantener inventario, evidencias y pendientes sin inflar la portada.
- SECURITY.md con límites y procedimiento de divulgación responsable cuando corresponda.
- CONTRIBUTING.md e incidencias guiadas con pasos de reproducción, versión, logs anonimizados y resultados esperados.

## Evidencia de software
- Capturas **reales** de UI obtenidas de ejecución del proyecto; incluir fuente de generación y nombre de la versión. Prohibido presentar renders o maquetas como pantallas verificadas.
- Tests unitarios y de integración con instrucciones ejecutables, además de CI cuando existan herramientas y recursos.
- No afirmar que una build funciona en Windows/Linux/hardware si solo se probó en un entorno distinto.
- Versiones y changelogs en la medida posible; no inferir releases/tags inexistentes.
- Reproducibilidad: datasets, hashes, splits, dependencias y procedencia de modelos cuando haya claims cuantitativos.

## Ingeniería responsable
- Separar observación, simulación y control real; la seguridad de maquinaria debe verificarse fuera del simulador.
- Marcar claramente modelos médicos y agronómicos como experimentales si no existe validación suficiente.
- No subir datos personales, secretos, claves, telemetría de terceros ni credenciales de cámaras o PLC.
- No mezclar código abierto con recursos cuyo régimen de propiedad intelectual no se haya verificado.

## Criterios mínimos para publicar nueva versión
1. Comandos de instalación y ejecución reproducibles.
2. Pruebas locales verificadas; CI preferible.
3. Imagen real de la interfaz, si dispone de UI, con origen identificado.
4. Nota de compatibilidad, limitaciones y permisos de uso.
5. Registro de cambios y comprobación de enlaces del README.

Revisión inicial del portafolio: **2026-10-22**. [Revisión actual de los 20 repositorios públicos](PORTFOLIO_REVIEW.md) · [Identidad visual y editorial](PORTFOLIO_IDENTITY.md). Esta política no certifica el funcionamiento de todos los proyectos.


## Control periódico automatizado

- El [workflow de calidad del portafolio](../.github/workflows/portfolio-quality.yml) revisa semanalmente los repositorios públicos a través de GitHub API.
- Su script reproducible está en [tools/portfolio_quality.py](../tools/portfolio_quality.py) y usa solo la biblioteca estándar de Python.
- El informe público versionado vive en [reports/portfolio-status.md](../reports/portfolio-status.md), con JSON para reanalizarlo.
- Una ejecución de CI satisfactoria verifica que el *control documental* se ejecutó; **no certifica el software de los proyectos**.
- Los resultados de investigación se siguen auditando en cada proyecto por sus propios protocolos.
