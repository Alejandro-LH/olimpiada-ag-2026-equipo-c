# Integrante 1 - Base del Proyecto y Funcion Objetivo

## Tu responsabilidad

Crea la estructura inicial del proyecto y programa la base del archivo principal.
Tu parte permite que los demas integrantes puedan agregar sus funciones encima.

## Archivos que debes crear

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
touch README.md
touch .gitignore
touch sesion1/equipo_C_codigo.py
touch sesion1/requirements.txt
touch docs/decisiones.md
```

Los nombres ya estan configurados para el Equipo C.

## Paso 1: Agrega las dependencias

En `sesion1/requirements.txt`, escribe:

```text
numpy
matplotlib
pandas
```

Esto sirve para que cualquier integrante pueda instalar las librerias necesarias.

## Paso 2: Agrega los imports

En `sesion1/equipo_C_codigo.py`, escribe al inicio:

```python
import csv
import os
import time
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np
```

Esto sirve para usar archivos CSV, tiempo de ejecucion, individuos, graficas y
calculos numericos.

## Paso 3: Agrega los parametros fijos

Debajo de los imports, escribe:

```python
POBLACION = 50
GENERACIONES = 100
LONGITUD_CROMOSOMA = 10
PROB_CRUZAMIENTO = 0.8
PROB_MUTACION = 0.01

LIMITE_INFERIOR = -5.12
LIMITE_SUPERIOR = 5.12
SEMILLA = 42
```

Esto sirve para respetar los parametros obligatorios del reto.

## Paso 4: Crea la estructura del individuo

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

```bash
git add .
git commit -m "Crear base del proyecto y funcion Rastrigin"
git push origin main
```

## Entregable de tu parte

Tu parte esta completa cuando:

- Existe la estructura de carpetas.
- Existe `equipo_C_codigo.py`.
- Existen `README.md`, `.gitignore`, `requirements.txt` y `docs/decisiones.md`.
- La funcion `rastrigin(np.zeros(10))` regresa `0.0`.
