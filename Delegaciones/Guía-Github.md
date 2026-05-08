# Guia Windows, Git y GitHub - Reto Sesion 1

Esta guia explica exactamente donde hacer cada cosa si el equipo trabaja en
Windows.

## 1. Datos que deben tener antes de empezar

Antes de abrir Git o GitHub, tengan estos datos:

```text
Letra del equipo: C
Nombre del repositorio: olimpiada-ag-2026-equipo-C
Correo del profesor: sebastiangz@ucol.mx
Nombre de los 6 integrantes
Correo de los 6 integrantes
Cuenta de GitHub de quien creara el repositorio
```

Los nombres ya estan configurados para el Equipo C.

Ejemplo:

```text
olimpiada-ag-2026-equipo-C
equipo_C_codigo.py
equipo_C_resultados.csv
equipo_C_grafica.png
```

## 2. Instalar Git en Windows

Esto se hace en el navegador.

1. Abre Google Chrome, Edge o Firefox.
2. Entra a:

```text
https://git-scm.com/download/win
```

3. Descarga Git para Windows.
4. Abre el instalador.
5. Deja las opciones por defecto.
6. Cuando termine, busca en el menu de inicio:

```text
Git Bash
```

Git Bash es la terminal donde escribiran los comandos de Git.

## 3. Instalar Python en Windows

Esto se hace en el navegador.

1. Entra a:

```text
https://www.python.org/downloads/
```

2. Descarga Python 3.
3. Abre el instalador.
4. Marca la casilla:

```text
Add python.exe to PATH
```

5. Da clic en `Install Now`.

Para comprobarlo, abre Git Bash y escribe:

```bash
python --version
```

Si no funciona, prueba:

```bash
py --version
```

## 4. Instalar VS Code

Esto se hace en el navegador.

1. Entra a:

```text
https://code.visualstudio.com/
```

2. Descarga VS Code.
3. Instala con opciones por defecto.

VS Code sirve para editar el codigo y los archivos `.md`.

## 5. Crear el repositorio en GitHub

Esto lo hace solo una persona, normalmente el Integrante 1 o Integrante 6.

Esto se hace en el navegador.

1. Entra a:

```text
https://github.com
```

2. Inicia sesion.
3. Da clic en el boton `+`.
4. Da clic en `New repository`.
5. En `Repository name`, escribe:

```text
olimpiada-ag-2026-equipo-C
```

6. Selecciona `Public`.
7. Marca `Add a README file`.
8. Da clic en `Create repository`.

## 6. Agregar al profesor como colaborador

Esto se hace en GitHub, dentro del repositorio.

1. Entra al repositorio.
2. Da clic en `Settings`.
3. En el menu izquierdo, entra a `Collaborators`.
4. Da clic en `Add people`.
5. Escribe:

```text
sebastiangz@ucol.mx
```

6. Envia la invitacion.

## 7. Copiar la URL del repositorio

Esto se hace en GitHub, dentro del repositorio.

1. Entra a la pagina principal del repo.
2. Da clic en el boton verde `Code`.
3. Copia la URL HTTPS.

Debe verse parecido a esto:

```text
https://github.com/TU_USUARIO/olimpiada-ag-2026-equipo-C.git
```

Esa URL se usara en Git Bash.

## 8. Clonar el repositorio en Windows

Esto se hace en Git Bash.

1. Abre `Git Bash`.
2. Ve a una carpeta facil, por ejemplo `Documents`:

```bash
cd Documents
```

3. Clona el repositorio:

```bash
git clone https://github.com/TU_USUARIO/olimpiada-ag-2026-equipo-C.git
```

4. Entra a la carpeta:

```bash
cd olimpiada-ag-2026-equipo-C
```

Todo lo que hagan del proyecto debe hacerse dentro de esta carpeta.

## 9. Configurar nombre y correo de Git

Esto se hace en Git Bash.

Cada integrante debe hacerlo una vez en su computadora:

```bash
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@ucol.mx"
```

Para revisar:

```bash
git config --list
```

## 10. Abrir el proyecto en VS Code

Esto se hace en Git Bash, estando dentro del repo.

Ejecuta:

```bash
code .
```

Si no funciona, abre VS Code manualmente:

1. Abre VS Code.
2. Da clic en `File`.
3. Da clic en `Open Folder`.
4. Selecciona la carpeta:

```text
olimpiada-ag-2026-equipo-C
```

## 11. Crear carpetas y archivos del reto

Esto se puede hacer en VS Code o en Git Bash.

En Git Bash:

```bash
mkdir sesion1
mkdir docs
touch sesion1/equipo_C_codigo.py
touch sesion1/requirements.txt
touch docs/decisiones.md
touch docs/integrante_1.md
touch docs/integrante_2.md
touch docs/integrante_3.md
touch docs/integrante_4.md
touch docs/integrante_5.md
touch docs/integrante_6.md
touch .gitignore
```

Si `touch` no funciona, creen los archivos desde VS Code:

1. Clic derecho sobre la carpeta.
2. `New File`.
3. Escriban el nombre del archivo.

## 12. Donde debe trabajar cada integrante

Todos editan el mismo archivo principal:

```text
sesion1/equipo_C_codigo.py
```

Pero cada integrante solo edita su bloque:

```text
Integrante 1:
imports, constantes, clase Individuo, funcion rastrigin

Integrante 2:
crear_individuo, crear_poblacion, evaluar_objetivo

Integrante 3:
fitness_inversion, fitness_negacion, fitness_ranking, asignar_fitness

Integrante 4:
seleccion_torneo, cruzamiento_un_punto, mutacion_uniforme, generar_nueva_poblacion

Integrante 5:
aplicar_elitismo, ejecutar_experimento

Integrante 6:
guardar_resultados_csv, guardar_grafica, main, README, entrega
```

Las instrucciones individuales estan en:

```text
docs/integrante_1.md
docs/integrante_2.md
docs/integrante_3.md
docs/integrante_4.md
docs/integrante_5.md
docs/integrante_6.md
```

## 13. Como trabajar sin pisarse

Opcion rapida si usan una sola computadora:

```text
Una persona escribe el codigo.
Cada integrante dicta o pega su bloque.
Despues de cada bloque hacen commit.
```

Opcion ordenada si cada quien usa su computadora:

Cada integrante crea su rama.

Esto se hace en Git Bash:

```bash
git pull origin main
git checkout -b integrante-1
```

Cada quien cambia el numero de su rama:

```bash
git checkout -b integrante-2
git checkout -b integrante-3
git checkout -b integrante-4
git checkout -b integrante-5
git checkout -b integrante-6
```

Cuando termine su parte:

```bash
git status
git add .
git commit -m "Agregar parte del integrante 1"
git push origin integrante-1
```

Despues se integran las ramas en GitHub usando Pull Request.

Si no saben usar Pull Request, usen una sola computadora para integrar mas
rapido.

## 14. Instalar librerias

Esto se hace en Git Bash, dentro del repo.

Primero entren a la carpeta del repo:

```bash
cd Documents/olimpiada-ag-2026-equipo-C
```

Luego instalen:

```bash
pip install -r sesion1/requirements.txt
```

Si `pip` no funciona, prueben:

```bash
python -m pip install -r sesion1/requirements.txt
```

O:

```bash
py -m pip install -r sesion1/requirements.txt
```

## 15. Ejecutar el codigo

Esto se hace en Git Bash.

Desde la raiz del repo:

```bash
cd sesion1
python equipo_C_codigo.py
```

Si `python` no funciona:

```bash
py equipo_C_codigo.py
```

El programa debe generar:

```text
equipo_C_resultados.csv
equipo_C_grafica.png
```

## 16. Revisar que el CSV este bien

Esto se hace en Git Bash, dentro de `sesion1`.

Ejecuta:

```bash
cat equipo_C_resultados.csv
```

Debe tener la primera linea:

```text
Transformacion,Elitismo,Mejor_Fitness,Generaciones,Tiempo_seg,Diversidad_Final
```

Y debe tener 9 filas de resultados.

## 17. Revisar la grafica

Esto se hace en el Explorador de archivos de Windows.

1. Abre la carpeta del repo.
2. Entra a `sesion1`.
3. Abre:

```text
equipo_C_grafica.png
```

Debe verse una grafica con 9 lineas.

## 18. Subir cambios a GitHub

Esto se hace en Git Bash, desde la raiz del repo.

Si estan dentro de `sesion1`, regresen a la raiz:

```bash
cd ..
```

Luego:

```bash
git status
git add .
git commit -m "Completar reto sesion 1"
git push origin main
```

Si estan trabajando en una rama, cambien `main` por el nombre de su rama.

## 19. Verificar en GitHub

Esto se hace en el navegador.

1. Entra a GitHub.
2. Abre el repositorio.
3. Verifica que existan:

```text
README.md
.gitignore
sesion1/equipo_C_codigo.py
sesion1/equipo_C_resultados.csv
sesion1/equipo_C_grafica.png
sesion1/requirements.txt
docs/decisiones.md
```

## 20. Obtener hash del ultimo commit

Esto se hace en Git Bash, desde la raiz del repo.

Ejecuta:

```bash
git log -1 --format="%H"
```

Copia el resultado. Ese texto largo es el hash que pide ELinea.

## 21. Entregar en ELinea

Esto se hace en el navegador.

1. Entra a ELinea.
2. Abre la actividad.
3. Pega la URL del repositorio GitHub.
4. Sube estos archivos:

```text
sesion1/equipo_C_codigo.py
sesion1/equipo_C_resultados.csv
sesion1/equipo_C_grafica.png
```

5. Pega el hash del ultimo commit.
6. Guarda la entrega.
7. Verifica que diga enviado o entregado.

## 22. Comandos resumen para Windows

Estos son los comandos principales en Git Bash:

```bash
cd Documents
git clone https://github.com/TU_USUARIO/olimpiada-ag-2026-equipo-C.git
cd olimpiada-ag-2026-equipo-C
git config --global user.name "Nombre Apellido"
git config --global user.email "correo@ucol.mx"
pip install -r sesion1/requirements.txt
cd sesion1
python equipo_C_codigo.py
cd ..
git status
git add .
git commit -m "Completar reto sesion 1"
git push origin main
git log -1 --format="%H"
