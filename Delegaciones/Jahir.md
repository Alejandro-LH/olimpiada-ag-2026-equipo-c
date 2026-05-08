# Integrante 1 - Base del Proyecto y Funcion Objetivo

## Tu responsabilidad

Crea la estructura inicial del proyecto y programa la base del archivo principal.
Tu parte permite que los demas integrantes puedan agregar sus funciones encima.

## Donde haras cada cosa

```text
GitHub: crear o abrir el repositorio.
Git Bash: crear carpetas, crear archivos y hacer commits.
VS Code: escribir codigo y editar archivos.
```

## Paso 0: Crea y abre el repositorio

Haz esto en `GitHub`, desde el navegador.

1. Entra a `https://github.com`.
2. Da clic en `+`.
3. Da clic en `New repository`.
4. En `Repository name`, escribe:

```text
olimpiada-ag-2026-equipo-C
```

5. Selecciona `Public`.
6. Marca `Add a README file`.
7. Da clic en `Create repository`.
8. En el boton verde `Code`, copia la URL HTTPS del repositorio.

Debe parecerse a esto:

```text
https://github.com/TU_USUARIO/olimpiada-ag-2026-equipo-C.git
```

Ahora haz esto en `Git Bash`.

```bash
cd Documents
git clone https://github.com/TU_USUARIO/olimpiada-ag-2026-equipo-C.git
cd olimpiada-ag-2026-equipo-C
code .
```

Si `code .` no funciona, abre `VS Code`, entra a `File > Open Folder` y selecciona
la carpeta `olimpiada-ag-2026-equipo-C`.

## Archivos que debes crear

Haz esto en `Git Bash`, dentro de la carpeta del repositorio.

Desde la raiz del repositorio, crea esta estructura:

```text
README.md
.gitignore
sesion1/
├── equipo_C_codigo.py
└── requirements.txt
docs/
└── decisiones.md
```

Usa estos comandos:

```bash
mkdir sesion1
mkdir docs
touch .gitignore
touch sesion1/equipo_C_codigo.py
touch sesion1/requirements.txt
touch docs/decisiones.md
```

Los nombres ya estan configurados para el Equipo C.

## Paso 1: Agrega las dependencias

Haz esto en `VS Code`.

En `sesion1/requirements.txt`, escribe:

```text
numpy
matplotlib
pandas
```

Esto sirve para que cualquier integrante pueda instalar las librerias necesarias.

## Paso 2: Agrega los imports

Haz esto en `VS Code`.

En `sesion1/equipo_C_codigo.py`, escribe al inicio:

```python
import csv
import os
import time
from dataclasses import dataclass

import numpy as np

LOCAL_CACHE_DIR = os.path.join(os.path.dirname(__file__), ".cache")
MPL_CACHE_DIR = os.path.join(os.path.dirname(__file__), ".mpl_cache")
os.makedirs(LOCAL_CACHE_DIR, exist_ok=True)
os.makedirs(MPL_CACHE_DIR, exist_ok=True)
os.environ.setdefault("XDG_CACHE_HOME", LOCAL_CACHE_DIR)
os.environ.setdefault("MPLCONFIGDIR", MPL_CACHE_DIR)

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
```

Esto sirve para usar archivos CSV, tiempo de ejecucion, individuos, graficas y
calculos numericos. La parte de cache y `Agg` sirve para que Matplotlib genere
la imagen correctamente en Windows aunque no se abra una ventana de grafica.

## Paso 3: Agrega los parametros fijos

Haz esto en `VS Code`, debajo de los imports.

Debajo de los imports, escribe:

```python
POBLACION = 50
GENERACIONES = 100
LONGITUD_CROMOSOMA = 10
PROB_CRUZAMIENTO = 0.8
PROB_MUTACION = 0.01
TIPO_SELECCION = "torneo"
TIPO_CRUZAMIENTO = "un_punto"
TIPO_MUTACION = "uniforme"

LIMITE_INFERIOR = -5.12
LIMITE_SUPERIOR = 5.12
SEMILLA = 42
```

Esto sirve para respetar los parametros obligatorios del reto.

## Paso 4: Crea la estructura del individuo

Haz esto en `VS Code`, debajo de los parametros.

Agrega:

```python
@dataclass
class Individuo:
    cromosoma: np.ndarray
    objetivo: float = 0.0
    fitness: float = 0.0
```

Esto sirve para guardar cada solucion del algoritmo genetico.

- `cromosoma`: los 10 numeros de la solucion.
- `objetivo`: valor de Rastrigin.
- `fitness`: valor usado para seleccionar individuos.

## Paso 5: Programa la funcion Rastrigin

Haz esto en `VS Code`, debajo de la clase `Individuo`.

Agrega:

```python
def rastrigin(x):
    A = 10
    n = len(x)
    return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))
```

Esto sirve para evaluar que tan buena es una solucion. El algoritmo busca que
este valor sea lo mas cercano posible a `0`.

## Paso 6: Prueba tu parte

Haz la prueba en `VS Code` y ejecutala desde `Git Bash`.

Al final del archivo, temporalmente puedes probar:

```python
if __name__ == "__main__":
    prueba = np.zeros(10)
    print(rastrigin(prueba))
```

Debe imprimir:

```text
0.0
```

Despues de probar, avisa al equipo que ya pueden continuar los demas.

## Paso 7: Haz commit

Haz esto en `Git Bash`, desde la raiz del repositorio.

```bash
git add .
git commit -m "Crear base del proyecto y funcion Rastrigin"
git push origin main
```

Despues de hacer `push`, entra al repositorio en `GitHub` y confirma que ya
aparecen los archivos.

## Entregable de tu parte

Tu parte esta completa cuando:

- Existe la estructura de carpetas.
- Existe `equipo_C_codigo.py`.
- Existen `README.md`, `.gitignore`, `requirements.txt` y `docs/decisiones.md`.
- La funcion `rastrigin(np.zeros(10))` regresa `0.0`.
