# Integrante 4 - Operadores Geneticos

## Tu responsabilidad

Programa los operadores geneticos: seleccion, cruzamiento, mutacion y creacion
de la nueva poblacion.

Estos operadores son los que producen nuevas soluciones a partir de la poblacion
actual.

No edites las transformaciones de fitness ni el elitismo.

## Donde haras cada cosa

```text
VS Code: escribir seleccion, cruza, mutacion y nueva poblacion.
Git Bash: ejecutar pruebas y hacer commit.
GitHub: confirmar que tu commit subio.
```

## Paso 0: Prepara tu copia del repositorio

Haz esto en `Git Bash`, antes de editar.

```bash
cd Documents/olimpiada-ag-2026-equipo-C
git pull origin main
code .
```

Si `code .` no funciona, abre la carpeta del proyecto desde `VS Code`.

## Paso 1: Programa seleccion por torneo

Haz esto en `VS Code`, debajo de `asignar_fitness`.

En `sesion1/equipo_C_codigo.py`, agrega:

```python
def seleccion_torneo(poblacion, k=3):
    participantes = np.random.choice(poblacion, size=k, replace=False)
    return max(participantes, key=lambda ind: ind.fitness)
```

Esto sirve para elegir padres. Se toman 3 candidatos al azar y gana el que tenga
mayor fitness.

## Paso 2: Programa cruzamiento de un punto

Haz esto en `VS Code`, debajo de `seleccion_torneo`.

Agrega:

```python
def cruzamiento_un_punto(padre1, padre2):
    if np.random.rand() > PROB_CRUZAMIENTO:
        return padre1.cromosoma.copy(), padre2.cromosoma.copy()

    punto = np.random.randint(1, LONGITUD_CROMOSOMA)
    hijo1 = np.concatenate([padre1.cromosoma[:punto], padre2.cromosoma[punto:]])
    hijo2 = np.concatenate([padre2.cromosoma[:punto], padre1.cromosoma[punto:]])
    return hijo1, hijo2
```

Esto sirve para mezclar dos soluciones y crear dos hijos.

## Paso 3: Programa mutacion uniforme

Haz esto en `VS Code`, debajo de `cruzamiento_un_punto`.

Agrega:

```python
def mutacion_uniforme(cromosoma):
    cromosoma_mutado = cromosoma.copy()

    for i in range(LONGITUD_CROMOSOMA):
        if np.random.rand() < PROB_MUTACION:
            cromosoma_mutado[i] = np.random.uniform(LIMITE_INFERIOR, LIMITE_SUPERIOR)

    return cromosoma_mutado
```

Esto sirve para cambiar genes al azar y explorar soluciones nuevas.

## Paso 4: Programa generacion de nueva poblacion

Haz esto en `VS Code`, debajo de `mutacion_uniforme`.

Agrega:

```python
def generar_nueva_poblacion(poblacion):
    nueva_poblacion = []

    while len(nueva_poblacion) < POBLACION:
        padre1 = seleccion_torneo(poblacion)
        padre2 = seleccion_torneo(poblacion)

        cromosoma_hijo1, cromosoma_hijo2 = cruzamiento_un_punto(padre1, padre2)
        cromosoma_hijo1 = mutacion_uniforme(cromosoma_hijo1)
        cromosoma_hijo2 = mutacion_uniforme(cromosoma_hijo2)

        nueva_poblacion.append(Individuo(cromosoma=cromosoma_hijo1))
        if len(nueva_poblacion) < POBLACION:
            nueva_poblacion.append(Individuo(cromosoma=cromosoma_hijo2))

    return nueva_poblacion
```

Esto sirve para crear una nueva generacion completa de 50 individuos.

## Paso 5: Prueba tu parte

Escribe esta prueba temporal en `VS Code` y ejecutala desde `Git Bash`.

Agrega temporalmente:

```python
if __name__ == "__main__":
    np.random.seed(42)
    poblacion = crear_poblacion()
    asignar_fitness(poblacion, "Inversion")
    nueva_poblacion = generar_nueva_poblacion(poblacion)

    print(len(nueva_poblacion))
    print(len(nueva_poblacion[0].cromosoma))
```

Debe imprimir:

```text
50
10
```

Quita la prueba temporal cuando se integre el `main`.

## Paso 6: Haz commit

Haz esto en `Git Bash`, desde la raiz del repositorio.

```bash
git add sesion1/equipo_C_codigo.py
git commit -m "Agregar operadores geneticos"
git push origin main
```

Despues entra a `GitHub` y revisa que tu commit aparezca en el repositorio.

## Entregable de tu parte

Tu parte esta completa cuando:

- La seleccion por torneo funciona con `k = 3`.
- El cruzamiento produce hijos de 10 genes.
- La mutacion mantiene valores dentro de `[-5.12, 5.12]`.
- `generar_nueva_poblacion()` regresa 50 individuos.
