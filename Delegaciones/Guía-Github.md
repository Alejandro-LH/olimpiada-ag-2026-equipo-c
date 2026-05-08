# Guia de Instalacion en Windows

Esta guia solo sirve para instalar y comprobar las herramientas. El trabajo
paso a paso esta repartido en `docs/integrante_1.md` a `docs/integrante_6.md`.

## 1. Instalar Git

Haz esto en el navegador.

1. Entra a:

```text
https://git-scm.com/download/win
```

2. Descarga Git para Windows.
3. Abre el instalador.
4. Deja las opciones por defecto.
5. Al terminar, busca en el menu de inicio:

```text
Git Bash
```

Git Bash sera la terminal para usar `git clone`, `git add`, `git commit` y
`git push`.

## 2. Instalar Python

Haz esto en el navegador.

1. Entra a:

```text
https://www.python.org/downloads/
```

2. Descarga Python 3.
3. Abre el instalador.
4. Marca esta casilla:

```text
Add python.exe to PATH
```

5. Da clic en `Install Now`.

Comprueba la instalacion en `Git Bash`:

```bash
python --version
```

Si no funciona, prueba:

```bash
py --version
```

## 3. Instalar VS Code

Haz esto en el navegador.

1. Entra a:

```text
https://code.visualstudio.com/
```

2. Descarga VS Code.
3. Instala con opciones por defecto.

VS Code se usara para editar:

```text
sesion1/equipo_C_codigo.py
README.md
docs/decisiones.md
```

## 4. Comprobar que todo esta listo

Abre `Git Bash` y ejecuta:

```bash
git --version
python --version
```

Si `python --version` no funciona, usa:

```bash
py --version
```

Si ambos comandos muestran una version, ya pueden seguir con las guias de los
integrantes.
