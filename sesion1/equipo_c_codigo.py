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

# crear una posible solucion con 10 numeros reales dentro del rango permitido
def crear_individuo():
    cromosoma = np.random.uniform(
        LIMITE_INFERIOR,
        LIMITE_SUPERIOR,
        size=LONGITUD_CROMOSOMA,
    )
    return Individuo(cromosoma=cromosoma)

# crear los 50 individuos que forman una generacion del algoritmo
# genetico.
def crear_poblacion():
    return [crear_individuo() for _ in range(POBLACION)]


""" para calcular el valor de Rastrigin de cada individuo. Mientras menor
sea este valor, mejor es la solucion """
def evaluar_objetivo(poblacion):
    for individuo in poblacion:
        individuo.objetivo = rastrigin(individuo.cromosoma)
        
if __name__ == "__main__":
    prueba = np.zeros(10)
    print(rastrigin(prueba))
    #Aarón
    np.random.seed(42)
    poblacion = crear_poblacion()
    evaluar_objetivo(poblacion)

    print(f'Población -> {len(poblacion)}')
    print(f'Cromosoma -> {len(poblacion[0].cromosoma)}')
    print(f'Poblacion -> {poblacion[0].objetivo}')
    #aqui termine (Aarón)
