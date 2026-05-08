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

@dataclass
class Individuo:
    cromosoma: np.ndarray
    objetivo: float = 0.0
    fitness: float = 0.0

def rastrigin(x):
    A = 10
    n = len(x)

    return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))

if __name__ == "__main__":
    prueba = np.zeros(10)
    print(rastrigin(prueba))


