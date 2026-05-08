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
        
#aqui termine (Aarón)

# valores pequeños de Rastrigin produzcan fitness mas alto.
def fitness_inversion(valor_objetivo):
    return 1.0 / (1.0 + valor_objetivo)

#convierte minimizacion a maximizacion usando como referencia el peor valor de la poblacion.
def fitness_negacion(valor_objetivo, c_max):
    return max(0.0, c_max - valor_objetivo)

# asigna fitness segun el lugar del individuo en la poblacion, sin depender directamente del valor numerico de Rastrigin.
def fitness_ranking(poblacion, sp=1.5):
    N = len(poblacion)
    fitness_dict = {}

    if N == 1:
        fitness_dict[0] = 1.0
        return fitness_dict

    for rank in range(1, N + 1):
        fitness = 2 - sp + 2 * (sp - 1) * (rank - 1) / (N - 1)
        fitness_dict[rank - 1] = fitness

    return fitness_dict

# el algoritmo pueda probar las 3 transformaciones sin cambiar el resto del codigo.
def asignar_fitness(poblacion, transformacion):
    evaluar_objetivo(poblacion)

    if transformacion == "Inversion":
        for individuo in poblacion:
            individuo.fitness = fitness_inversion(individuo.objetivo)

    elif transformacion == "Negacion":
        peor_objetivo = max(individuo.objetivo for individuo in poblacion)
        c_max = peor_objetivo * 1.1
        for individuo in poblacion:
            individuo.fitness = fitness_negacion(individuo.objetivo, c_max)

    elif transformacion == "Ranking":
        poblacion_ordenada = sorted(poblacion, key=lambda ind: ind.objetivo, reverse=True)
        ranking = fitness_ranking(poblacion_ordenada)
        for indice, individuo in enumerate(poblacion_ordenada):
            individuo.fitness = ranking[indice]

    else:
        raise ValueError(f"Transformacion desconocida: {transformacion}")
# Aquí termine (Cesar)

def seleccion_torneo(poblacion, k=3):
    participantes = np.random.choice(poblacion, size=k, replace=False)
    return max(participantes, key=lambda ind: ind.fitness)

def cruzamiento_un_punto(padre1, padre2):
    if np.random.rand() > PROB_CRUZAMIENTO:
        return padre1.cromosoma.copy(), padre2.cromosoma.copy()

    punto = np.random.randint(1, LONGITUD_CROMOSOMA)

    hijo1 = np.concatenate([
        padre1.cromosoma[:punto],
        padre2.cromosoma[punto:]
    ])

    hijo2 = np.concatenate([
        padre2.cromosoma[:punto],
        padre1.cromosoma[punto:]
    ])

    return hijo1, hijo2

def mutacion_uniforme(cromosoma):
    cromosoma_mutado = cromosoma.copy()

    for i in range(LONGITUD_CROMOSOMA):
        if np.random.rand() < PROB_MUTACION:
            cromosoma_mutado[i] = np.random.uniform(
                LIMITE_INFERIOR,
                LIMITE_SUPERIOR
            )

    return cromosoma_mutado

def generar_nueva_poblacion(poblacion):
    nueva_poblacion = []

    while len(nueva_poblacion) < POBLACION:

        padre1 = seleccion_torneo(poblacion)
        padre2 = seleccion_torneo(poblacion)

        cromosoma_hijo1, cromosoma_hijo2 = cruzamiento_un_punto(
            padre1,
            padre2
        )

        cromosoma_hijo1 = mutacion_uniforme(cromosoma_hijo1)
        cromosoma_hijo2 = mutacion_uniforme(cromosoma_hijo2)

        nueva_poblacion.append(
            Individuo(cromosoma=cromosoma_hijo1)
        )

        if len(nueva_poblacion) < POBLACION:
            nueva_poblacion.append(
                Individuo(cromosoma=cromosoma_hijo2)
            )

    return nueva_poblacion
# Aquí termine (Lalo)

