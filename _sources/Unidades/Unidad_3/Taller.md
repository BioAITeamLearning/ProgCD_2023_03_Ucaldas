# 📄 Taller 

## Ejercicio

Reinel Tabares Soto

:::{note}
Este Taller debe entregarse como un notebook en Google Colaboratory, completamente documentado y paso a paso, con cero errores de compilación.
:::

### Ejercicio 1
Demostrar la Ley de Amdahl y la eficiencia, graficar en python las funciones variando el porcentaje de código no paralelizable y la cantidad de procesadores teniendo en cuenta la siguiente información:
Las ecuaciones se definen de la siguiente manera:

$$
S(N) = \frac{T}{TP(N)}
$$

Donde:
- $S(N)$ es el Speed-Up.
- $T$ es el tiempo de ejecución en secuencial.
- $TP(N)$ es el tiempo de ejecución paralelo.

$$
T = s + p
$$

Donde:
- $T$ es el tiempo de ejecución en secuencial.
- $s$ es la parte de código secuencial.
- $p$ es la parte de código paralelizable.

$$
E(N) = \frac{S(N)}{N}
$$

Donde:
- $E(N)$ es la Eficiencia.
- $S(N)$ es el Speed-Up.
- $N$ es el número de procesadores.

Además, se mencionan las siguientes variables:
- $T$ es el tiempo de ejecución en secuencial.
- $TP(N)$ es el tiempo de ejecución paralelo.
- $s$ es la parte de código secuencial.
- $p$ es la parte de código paralelizable.
- $N$ es el número de procesadores.
- $f$ es la fracción de código no paralelizable.

### Ejercicio 2
Si se aumenta indefinidamente el número de procesadores como se interpreta la ley de Amdahl y la eficiencia?

### Ejercicio 3
Si se aumenta la fracción secuencial para un número determinado de procesadores qué se puede concluir?

### Ejercicio 4
Qué pasa con un sistema que tiene 16 procesadores cuando sobre él se ejecuta un proceso con un 25% no paralelizable?
