# 📄 Ejercicio

Reinel Tabares Soto

:::{note}
Este Taller debe entregarse como un notebook en Google Colaboratory, completamente documentado y paso a paso, con cero errores de compilación.
:::

```{tip}
<a href="https://www.infor.uva.es/~bastida/Arquitecturas%20Avanzadas/General.pdf" target="_blank">Recurso de apoyo</a>
```

### Ejercicio a
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

### Ejercicio b
Si se aumenta indefinidamente el número de procesadores como se interpreta la ley de Amdahl y la eficiencia?

### Ejercicio c
Si se aumenta la fracción secuencial para un número determinado de procesadores qué se puede concluir?

### Ejercicio d
Qué pasa con un sistema que tiene 16 procesadores cuando sobre él se ejecuta un proceso con un 25% no paralelizable?
