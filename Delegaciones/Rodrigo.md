# Integrante 6 - CSV, Grafica, GitHub y Entrega

## Tu responsabilidad

Programa la salida final del proyecto: CSV, grafica y `main`. Tambien coordina
GitHub y la entrega en ELinea.

Tu parte convierte los experimentos en archivos entregables.

No edites las funciones internas del algoritmo salvo que haya un error avisado
por el equipo.

## Donde haras cada cosa

```text
VS Code: escribir CSV, grafica, main y completar README.
Git Bash: instalar dependencias, ejecutar codigo, revisar CSV y hacer commits.
GitHub: revisar repo publico, archivos subidos y colaborador del profesor.
ELinea: subir codigo, CSV, grafica, URL y hash final.
```

## Paso 0: Prepara tu copia del repositorio

Haz esto en `Git Bash`, antes de editar.

```bash
cd Documents/olimpiada-ag-2026-equipo-C
git pull origin main
code .
```

Si `code .` no funciona, abre la carpeta del proyecto desde `VS Code`.

## Paso 1: Define nombres de archivos

Haz esto en `VS Code`, cerca de las constantes del archivo.

En `sesion1/equipo_C_codigo.py`, agrega cerca de las constantes:

```python
ARCHIVO_CSV = "equipo_C_resultados.csv"
ARCHIVO_GRAFICA = "equipo_C_grafica.png"
```

Los nombres ya estan configurados para el Equipo C.

Esto sirve para que el programa genere los archivos con el nombre correcto.

## Paso 2: Programa guardado de CSV

Haz esto en `VS Code`, debajo de `ejecutar_experimento`.

Agrega:

```python
def guardar_resultados_csv(resultados):
    columnas = [
        "Transformacion",
        "Elitismo",
        "Mejor_Fitness",
        "Generaciones",
        "Tiempo_seg",
        "Diversidad_Final",
    ]

    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=columnas)
        writer.writeheader()

        for fila in resultados:
            writer.writerow(
                {
                    "Transformacion": fila["Transformacion"],
                    "Elitismo": fila["Elitismo"],
                    "Mejor_Fitness": f"{fila['Mejor_Fitness']:.6f}",
                    "Generaciones": fila["Generaciones"],
                    "Tiempo_seg": f"{fila['Tiempo_seg']:.4f}",
                    "Diversidad_Final": f"{fila['Diversidad_Final']:.6f}",
                }
            )
```

Esto sirve para crear `equipo_C_resultados.csv` con las 9 configuraciones.

## Paso 3: Programa la grafica

Haz esto en `VS Code`, debajo de `guardar_resultados_csv`.

Agrega:

```python
def guardar_grafica(historiales):
    generaciones = list(range(GENERACIONES + 1))

    plt.figure(figsize=(12, 8))

    for etiqueta, historial in historiales.items():
        plt.plot(generaciones, historial, label=etiqueta, linewidth=2)

    plt.xlabel("Generacion", fontsize=12)
    plt.ylabel("Mejor Fitness", fontsize=12)
    plt.title("Convergencia: Transformaciones de Fitness x Elitismo", fontsize=14)
    plt.legend(loc="best", fontsize=9)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(ARCHIVO_GRAFICA, dpi=300, bbox_inches="tight")
    plt.close()
```

Esto sirve para crear `equipo_C_grafica.png` con las 9 lineas de convergencia.

## Paso 4: Programa el main

Haz esto en `VS Code`, al final de `equipo_C_codigo.py`.

Agrega:

```python
def main():
    transformaciones = ["Inversion", "Negacion", "Ranking"]
    niveles_elitismo = [0, 2, 5]

    resultados = []
    historiales = {}

    for transformacion in transformaciones:
        for elitismo in niveles_elitismo:
            resultado, historial = ejecutar_experimento(transformacion, elitismo)
            resultados.append(resultado)
            historiales[f"{transformacion} k={elitismo}"] = historial

            print(
                f"{transformacion:9s} | k={elitismo} | "
                f"Mejor fitness={resultado['Mejor_Fitness']:.6f} | "
                f"Tiempo={resultado['Tiempo_seg']:.4f}s | "
                f"Diversidad={resultado['Diversidad_Final']:.6f}"
            )

    guardar_resultados_csv(resultados)
    guardar_grafica(historiales)

    print(f"\nCSV generado: {ARCHIVO_CSV}")
    print(f"Grafica generada: {ARCHIVO_GRAFICA}")


if __name__ == "__main__":
    main()
```

Esto sirve para ejecutar automaticamente las 9 combinaciones:

```text
Inversion k=0, 2, 5
Negacion k=0, 2, 5
Ranking k=0, 2, 5
```

## Paso 5: Ejecuta el codigo

Haz esto en `Git Bash`.

Desde la raiz del repositorio:

```bash
pip install -r sesion1/requirements.txt
cd sesion1
python equipo_C_codigo.py
```

Debe generar:

```text
equipo_C_resultados.csv
equipo_C_grafica.png
```

Antes de ejecutar la version final, revisa que los integrantes 1 a 5 hayan
quitado sus pruebas temporales. En el archivo final solo debe quedar este bloque
al final:

```python
if __name__ == "__main__":
    main()
```

Esto evita que el programa imprima pruebas sueltas o se ejecute por partes antes
de generar el CSV y la grafica.

## Paso 6: Revisa el CSV

Haz esto en `Git Bash`, dentro de la carpeta `sesion1`.

Ejecuta:

```bash
cat equipo_C_resultados.csv
```

Debe tener estas columnas:

```text
Transformacion,Elitismo,Mejor_Fitness,Generaciones,Tiempo_seg,Diversidad_Final
```

Debe tener 9 filas de resultados.

## Paso 7: Revisa la grafica

Haz esto en el `Explorador de archivos de Windows` o desde `VS Code`.

Abre `equipo_C_grafica.png`.

Debe tener:

- 9 lineas.
- Eje X: generaciones.
- Eje Y: mejor fitness.
- Leyenda clara.
- Titulo.
- Grid.

## Paso 8: Completa README

Haz esto en `VS Code`.

En `README.md`, asegúrate de incluir:

- Nombre del equipo.
- Integrantes.
- Descripcion del proyecto.
- Requisitos.
- Como ejecutar.
- Donde estan los resultados.

## Paso 9: Sube a GitHub

Haz esto en `Git Bash`, desde la raiz del repositorio.

Ejecuta desde la raiz del repositorio:

```bash
git status
git add .
git commit -m "Generar resultados finales y documentacion"
git push origin main
```

Ahora haz esto en `GitHub`, desde el navegador.

1. Entra al repositorio `olimpiada-ag-2026-equipo-C`.
2. Confirma que existan:

```text
README.md
.gitignore
sesion1/equipo_C_codigo.py
sesion1/equipo_C_resultados.csv
sesion1/equipo_C_grafica.png
sesion1/requirements.txt
docs/decisiones.md
```

3. Entra a `Settings > Collaborators`.
4. Agrega al profesor:

```text
sebastiangz@ucol.mx
```

## Paso 10: Obtén el hash final

Haz esto en `Git Bash`, desde la raiz del repositorio.

Ejecuta:

```bash
git log -1 --format="%H"
```

Copia ese hash. Se entrega en ELinea.

## Paso 11: Entrega en ELinea

Haz esto en el `navegador`, dentro de ELinea.

Sube estos archivos:

```text
sesion1/equipo_C_codigo.py
sesion1/equipo_C_resultados.csv
sesion1/equipo_C_grafica.png
```

Tambien pega:

```text
URL del repositorio GitHub
Hash del ultimo commit
```

## Entregable de tu parte

Tu parte esta completa cuando:

- El programa corre sin errores.
- El CSV existe y tiene 9 filas.
- La grafica existe y tiene 9 lineas.
- No quedan pruebas temporales de otros integrantes en el archivo final.
- El README esta completo.
- El repo es publico.
- El profesor fue agregado como colaborador.
- El hash final fue copiado.
- La entrega en ELinea quedo enviada.
