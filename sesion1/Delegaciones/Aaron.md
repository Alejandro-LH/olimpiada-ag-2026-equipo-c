# Integrante 2 - Poblacion Inicial y Evaluacion

## Tu responsabilidad

Programa las funciones que crean individuos, crean la poblacion inicial y
calculan el valor objetivo de cada individuo.

No edites las funciones del Integrante 1. Trabaja debajo de `rastrigin`.

## Donde haras cada cosa

```text
VS Code: escribir tus funciones en equipo_C_codigo.py.
Git Bash: ejecutar pruebas y hacer commit.
GitHub: verificar que tu commit subio.
```

## Paso 0: Prepara tu copia del repositorio

Haz esto en `Git Bash`, antes de editar.

```bash
cd Documents/olimpiada-ag-2026-equipo-C
git pull origin main
code .
```

Si `code .` no funciona, abre la carpeta del proyecto desde `VS Code`.

## Paso 1: Crea un individuo

Haz esto en `VS Code`, debajo de `rastrigin`.

En `sesion1/equipo_C_codigo.py`, agrega:

```python
def crear_individuo():
    cromosoma = np.random.uniform(
        LIMITE_INFERIOR,
        LIMITE_SUPERIOR,
        size=LONGITUD_CROMOSOMA,
    )
    return Individuo(cromosoma=cromosoma)
```

Esto sirve para crear una posible solucion con 10 numeros reales dentro del
rango permitido `[-5.12, 5.12]`.

## Paso 2: Crea la poblacion

Haz esto en `VS Code`, debajo de `crear_individuo`.

Agrega:

```python
def crear_poblacion():
    return [crear_individuo() for _ in range(POBLACION)]
```

Esto sirve para crear los 50 individuos que forman una generacion del algoritmo
genetico.

## Paso 3: Evalua la funcion objetivo

Haz esto en `VS Code`, debajo de `crear_poblacion`.

Agrega:

```python
def evaluar_objetivo(poblacion):
    for individuo in poblacion:
        individuo.objetivo = rastrigin(individuo.cromosoma)
```

Esto sirve para calcular el valor de Rastrigin de cada individuo. Mientras menor
sea este valor, mejor es la solucion.

## Paso 4: Prueba tu parte

Escribe esta prueba temporal en `VS Code` y ejecutala desde `Git Bash`.

Agrega temporalmente al final del archivo:

```python
if __name__ == "__main__":
    np.random.seed(42)
    poblacion = crear_poblacion()
    evaluar_objetivo(poblacion)

    print(len(poblacion))
    print(len(poblacion[0].cromosoma))
    print(poblacion[0].objetivo)
```

Debe cumplirse:

```text
La poblacion tiene 50 individuos.
Cada cromosoma tiene 10 valores.
El objetivo del primer individuo es un numero.
```

Quita la prueba temporal cuando el equipo integre el `main` final.

## Paso 5: Haz commit

Haz esto en `Git Bash`, desde la raiz del repositorio.

```bash
git add sesion1/equipo_C_codigo.py
git commit -m "Agregar poblacion inicial y evaluacion objetivo"
git push origin main
```

Despues entra a `GitHub` y revisa que tu commit aparezca en el repositorio.

## Entregable de tu parte

Tu parte esta completa cuando:

- `crear_individuo()` crea un individuo valido.
- `crear_poblacion()` crea 50 individuos.
- `evaluar_objetivo()` calcula Rastrigin para todos.
- No cambiaste los parametros fijos del reto.
