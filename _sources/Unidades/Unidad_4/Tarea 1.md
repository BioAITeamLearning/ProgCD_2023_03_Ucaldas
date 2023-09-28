# Tarea 1

Reinel Tabares Soto

:::{note}
Se premiará la solución correcta con un BONUS en una calificación.
:::

Teniendo en cuenta los conceptos vistos en esta clase, implemente un algoritmo que ejecute hilos para realizar el proceso de la multiplicación de matrices de manera concurrente. 

:::{tip}
Ojo leer capítulo 2 del cookbook
:::

**1.** Realice una función que tome una fila y una columna y las multiplique.

**2.** Esta función es la que debe enviarse a cada uno de los hilos y ejecutarse concurrentemente hasta completar todas las operaciones necesarias.

**3.** Realice la ejecución del algoritmo primero solo lanzando dos hilos cada vez. Luego 4 hilos, 8 hilos y finalmente 16 hilos.

**4.** Para cada uno de los casos del punto anterior, calcule los tiempos totales de la ejecución de la multiplicación de las matrices y el speed-up.

**5.** Realice las gráficas de aceleración para cada caso (número de hilos).

```{warning}
Si la función del punto 1 No emplea una multiplicación de fila-columna sino dos filas y dos columnas, realice todos los puntos anteriores de implementación y compare los resultados
```
