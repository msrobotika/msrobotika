# Publicación propia en GitHub (MS ROBOTIKA)

La aplicación fue preparada como repositorio independiente. Crear el repositorio nuevo requiere un permiso de GitHub que la integración del chat no tiene concedido actualmente; **no afirmamos que el proyecto esté ya publicado**.

1. En la cuenta GitHub `msrobotika`, crea un **repositorio público vacío** llamado `AB-Vision-Inspector` (no selecciones README, .gitignore ni licencia automática porque ya van incluidos).
2. Descomprime el ZIP completo y entra en la carpeta `AB-Vision-Inspector`.
3. Con Git instalado, ejecuta estos comandos (en PowerShell, CMD o consola Linux):

```sh
git init
git add .
git commit -m "feat: feat: AB-Vision Inspector 0.3 camera audit with verified screenshots"
git branch -M main
git remote add origin https://github.com/msrobotika/AB-Vision-Inspector.git
git push -u origin main
```

Si Git solicita credenciales, inicia sesión con Git Credential Manager o utiliza un token personal bajo tu propio control. **No compartas tokens por chat.**

4. Comprueba que el README de la rama `main` **muestra las cuatro capturas reales** (archivos PNG ya incorporados al ZIP en `docs/screenshots/`).
5. Abre `Actions` y comprueba que las pruebas de código y navegador finalizan correctamente. Verifica primero la seguridad y la licencia antes de publicar releases comerciales.

**Importante**: no publiques en los repositorios existentes de AB-Modbus o AB-BI: esta aplicación debe ser un proyecto separado. No incorpores un `.env`, tokens, archivos privados ni capturas ajenas al paquete.