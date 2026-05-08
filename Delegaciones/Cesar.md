# Integrante 3 - Transformaciones de Fitness

## Tu responsabilidad

Programa las 3 transformaciones que convierten el valor objetivo a fitness.

Rastrigin se minimiza, pero el algoritmo genetico selecciona individuos con
fitness alto. Tus funciones hacen esa conversion.

No edites poblacion, operadores geneticos ni elitismo.

## Donde haras cada cosa

```text
VS Code: escribir las funciones de fitness.
Git Bash: correr pruebas y hacer commit.
GitHub: revisar que tu cambio aparezca en el repositorio.
```

## Paso 0: Prepara tu copia del repositorio

Haz esto en `Git Bash`, antes de editar.

```bash
cd Documents/olimpiada-ag-2026-equipo-C
git pull origin main
code .
```

Si `code .` no funciona, abre la carpeta del proyecto desde `VS Code`.

## Paso 1: Programa inversion simple

Haz esto en `VS Code`, debajo de las funciones de poblacion.

En `sesion1/equipo_C_codigo.py`, agrega:

```python
def fitness_inversion(valor_objetivo):
    return 1.0 / (1.0 + valor_objetivo)
```

Esto sirve para que valores pequenos de Rastrigin produzcan fitness mas alto.

## Paso 2: Programa negacion con desplazamiento

Haz esto en `VS Code`, debajo de `fitness_inversion`.

Agrega:

```python
def fitness_negacion(valor_objetivo, c_max):
    return max(0.0, c_max - valor_objetivo)
```

Esto sirve para convertir minimizacion a maximizacion usando como referencia el
peor valor de la poblacion.

## Paso 3: Programa ranking lineal

Haz esto en `VS Code`, debajo de `fitness_negacion`.

Agrega:

```python
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
```

Esto sirve para asignar fitness segun el lugar del individuo en la poblacion,
sin depender directamente del valor numerico de Rastrigin.

## Paso 4: Programa asignacion de fitness

Haz esto en `VS Code`, debajo de `fitness_ranking`.

Agrega:

```python
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
```

Esto sirve para que el mismo algoritmo pueda probar las 3 transformaciones sin
cambiar el resto del codigo.

## Paso 5: Prueba tu parte

Escribe esta prueba temporal en `VS Code` y ejecutala desde `Git Bash`.

Agrega temporalmente:

```python
if __name__ == "__main__":
    np.random.seed(42)
    poblacion = crear_poblacion()

    for transformacion in ["Inversion", "Negacion", "Ranking"]:
        asignar_fitness(poblacion, transformacion)
        fitness = [ind.fitness for ind in poblacion]
        print(transformacion, min(fitness), max(fitness))
```

Debe cumplirse:

```text
Las 3 transformaciones imprimen valores de fitness.
Todos los fitness son mayores o iguales a 0.
```

Quita la prueba temporal cuando se integre el `main`.

## Paso 6: Haz commit

Haz esto en `Git Bash`, desde la raiz del repositorio.

```bash
git add sesion1/equipo_C_codigo.py
git commit -m "Implementar transformaciones de fitness"
git push origin main
```

Despues entra a `GitHub` y revisa que tu commit aparezca en el repositorio.

## Entregable de tu parte

Tu parte esta completa cuando:

- Existen las 3 funciones de fitness.
- `asignar_fitness()` funciona con `"Inversion"`, `"Negacion"` y `"Ranking"`.
- Todos los individuos reciben fitness.
