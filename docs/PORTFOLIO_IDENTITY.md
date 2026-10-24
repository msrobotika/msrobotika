# Identidad de MS ROBOTIKA · Portfolio identity

La identidad ayuda a reconocer un proyecto y encontrar su primer uso. No sustituye al producto ni a sus pruebas.

## Sistema visual · Visual system

- Cabeceras SVG propias en [assets/projects](../assets/projects), con texto accesible, sin fuentes remotas, scripts ni imágenes generadas que aparenten ser capturas.
- Fondo `#111820`, texto `#f4f7fb` y un acento por familia: azul para AB Suite/Android, turquesa para dispositivos, violeta para investigación y verde suave para experimentos.
- Un nombre, una función y una familia por cabecera. Sin versiones incrustadas en la imagen: el estado se mantiene como texto editable en la portada.
- Las capturas muestran ejecución real y declaran su procedencia. Una maqueta se etiqueta como vista previa. Una captura de AB Suite en un repositorio de origen indica expresamente que pertenece a la edición integrada.

## Entrada de cada proyecto · Project entry

1. Nombre y propósito breve en español e inglés.
2. Acceso visible a instalación o primer uso, documentación y estado.
3. Requisitos reales: modelos externos, Git LFS, herramientas de desarrollo o hardware compatible antes del comando de ejecución.
4. Funciones disponibles separadas de la hoja de ruta.
5. Licencias y evidencia enlazadas desde archivos existentes.

La suite usa una descarga común y su catálogo muestra las nueve herramientas. Los repositorios de origen preservan fuentes e historial y dirigen a esa distribución. Los proyectos independientes mantienen su instalación propia.

## Mantenimiento · Maintenance

Actualizar README, About y Website cuando cambie el punto de entrada. No usar una dirección local como demo pública ni una versión antigua como descarga recomendada. Revisar enlaces con `tools/portfolio_quality.py` y la entrada de la suite con `tools/check_featured_profile.py`.

CI siempre tiene nombre, revisión y alcance: sintaxis, algoritmo, navegador, instalación o dispositivo. Un workflow correcto no significa que todos los demás hayan pasado. Una ejecución histórica no verifica el HEAD actual.

English: use original accessible headers, a short bilingual purpose, visible first-use instructions, explicit prerequisites, accurate capabilities and revision-bound evidence. Keep independent projects distinct while directing all nine suite tools to the shared distribution.
