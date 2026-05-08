# Integrante 5 - Elitismo y Ejecucion de Experimentos

## Tu responsabilidad

Programa el elitismo y la funcion que ejecuta un experimento completo durante
100 generaciones.

Tu parte une la poblacion, el fitness y los operadores geneticos.

No edites la grafica ni el CSV.

## Donde haras cada cosa

```text
VS Code: escribir elitismo y ejecucion de experimento.
Git Bash: probar una configuracion y hacer commit.
GitHub: verificar que tu parte quedo subida.
```

## Paso 0: Prepara tu copia del repositorio

Haz esto en `Git Bash`, antes de editar.

```bash
cd Documents/olimpiada-ag-2026-equipo-C
git pull origin main
code .
```

Si `code .` no funciona, abre la carpeta del proyecto desde `VS Code`.

## Paso 1: Programa elitismo

Haz esto en `VS Code`, debajo de `generar_nueva_poblacion`.

En `sesion1/equipo_C_codigo.py`, agrega:

```python
def aplicar_elitismo(poblacion_actual, nueva_poblacion, k):
    if k == 0:
        return nueva_poblacion

    poblacion_actual_ordenada = sorted(
        poblacion_actual,
        key=lambda ind: ind.fitness,
        reverse=True,
    )

    elites = [
        Individuo(
            cromosoma=ind.cromosoma.copy(),
            objetivo=ind.objetivo,
            fitness=ind.fitness,
        )
        for ind in poblacion_actual_ordenada[:k]
    ]

    nueva_poblacion_ordenada = sorted(
        nueva_poblacion,
        key=lambda ind: ind.fitness,
        reverse=True,
    )

    return elites + nueva_poblacion_ordenada[: len(nueva_poblacion) - k]
```

Esto sirve para conservar los mejores individuos de una generacion.

- `k = 0`: no conserva elites.
- `k = 2`: conserva los 2 mejores.
- `k = 5`: conserva los 5 mejores.

## Paso 2: Programa un experimento completo

Haz esto en `VS Code`, debajo de `aplicar_elitismo`.

Agrega:

```python
def ejecutar_experimento(transformacion, elitismo):
    np.random.seed(SEMILLA)
    inicio = time.perf_counter()

    poblacion = crear_poblacion()
    asignar_fitness(poblacion, transformacion)

    historial_mejor_fitness = [max(ind.fitness for ind in poblacion)]

    for _ in range(GENERACIONES):
        nueva_poblacion = generar_nueva_poblacion(poblacion)
        asignar_fitness(nueva_poblacion, transformacion)
        poblacion = aplicar_elitismo(poblacion, nueva_poblacion, elitismo)
        asignar_fitness(poblacion, transformacion)

        mejor_fitness = max(ind.fitness for ind in poblacion)
        historial_mejor_fitness.append(mejor_fitness)

    tiempo_seg = time.perf_counter() - inicio

    resultado = {
        "Transformacion": transformacion,
        "Elitismo": elitismo,
        "Mejor_Fitness": max(ind.fitness for ind in poblacion),
        "Generaciones": GENERACIONES,
        "Tiempo_seg": tiempo_seg,
        "Diversidad_Final": float(np.std([ind.fitness for ind in poblacion])),
    }

    return resultado, historial_mejor_fitness
```

Esto sirve para correr una configuracion completa:

```text
1 transformacion + 1 nivel de elitismo
```

Ejemplo:

```text
Inversion con k = 2
```

## Paso 3: Revisa las metricas

Haz esta revision en `VS Code`, leyendo el diccionario `resultado`.

El diccionario `resultado` debe guardar:

- `Transformacion`: nombre de la transformacion usada.
- `Elitismo`: valor de k.
- `Mejor_Fitness`: mejor fitness al final.
- `Generaciones`: siempre 100.
- `Tiempo_seg`: tiempo que tardo.
- `Diversidad_Final`: desviacion estandar del fitness final.

## Paso 4: Prueba tu parte

Escribe esta prueba temporal en `VS Code` y ejecutala desde `Git Bash`.

Agrega temporalmente:

```python
if __name__ == "__main__":
    resultado, historial = ejecutar_experimento("Inversion", 2)
    print(resultado)
    print(len(historial))
```

Debe cumplirse:

```text
El resultado muestra una configuracion.
El historial tiene 101 valores: generacion 0 a generacion 100.
```

Quita la prueba temporal cuando se integre el `main`.

## Paso 5: Haz commit

Haz esto en `Git Bash`, desde la raiz del repositorio.

```bash
git add sesion1/equipo_C_codigo.py
git commit -m "Implementar elitismo y experimentos"
git push origin main
```

Despues entra a `GitHub` y revisa que tu commit aparezca en el repositorio.

## Entregable de tu parte

Tu parte esta completa cuando:

- `aplicar_elitismo()` funciona con `k = 0`, `k = 2` y `k = 5`.
- `ejecutar_experimento()` corre 100 generaciones.
- El historial tiene 101 valores.
- El resultado incluye todas las columnas requeridas para el CSV.
