---
title: Unidad 3
---
# Unidad 3: Métricas de desempeño

## Contenido de la unidad

<img src="_static/images/contenidoU3.png"/>

## Tiempo, aceleración, eficiencia y escalabilidad
¿Cómo evaluar el desempeño de un programa paralelo?

### Tiempo de ejecución

Es el índice más básico. Se define como el intervalo de tiempo que transcurre desde el comienzo de la ejecución de la aplicación en el sistema paralelo hasta que el último proceso termina su ejecución.

<img src="_static/images/U2_23.jpg"/>

Esta métrica es absoluta y permite medir el programa paralelo sin necesidad de compararlo con otro.

### Aceleración

La fórmula del Speed-Up se define como:

$$
Speed_{Up} = \frac{T \cdot n}{T_p(N)}
$$

Donde:
- $T \cdot n$ representa el mejor tiempo de ejecución en modo secuencial.
- $T_p(N)$ representa el tiempo de ejecución en modo paralelo.

```{dropdown} Aceleración

<img src="_static/images/U2_24.jpg"/>

```

- La aceleración varía de una máquina paralela a otra y en función de cómo se realice la paralelización. 

- Un mayor speedup es igual a más ganancia con la paralelización. 

### Eficiencia

La eficiencia se calcula utilizando la siguiente fórmula:

$$
Eficiencia(p) = \frac{Speed\_up(p)}{p}
$$

Donde:
- $Eficiencia(p)$ es la eficiencia con $p$ procesos. Con un valor entre 0 y 1. Su rendimiento puede verse afectado por el **overhead**.
- $Speed\_up(p)$ es el speed-up con $p$ procesos.
- $p$ es la cantidad de procesos con los que se ejecuta la aplicación. 

```{dropdown} Eficiencia

<img src="_static/images/U2_25.jpg"/>

**Paralelización y Eficiencia:**
1. Idealmente, se espera una eficiencia de 1 en la paralelización, lo que significa que se ha logrado una paralelización total.
2. En la práctica, no todo el programa puede ser paralelizado.

**Overhead:**
- El overhead se refiere al costo adicional asociado con la administración de la comunicación y sincronización entre procesos en la programación paralela.
- Puede limitar la escalabilidad de un algoritmo y afectar el rendimiento.
- El overhead incluye factores como el tiempo de inicio y terminación de tareas, sincronización, comunicación de datos y sobrecarga de software (lenguajes paralelos, bibliotecas, sistema operativo, etc.).
- Es importante minimizar el overhead siempre que sea posible para lograr un alto rendimiento y una buena escalabilidad.

```

### Escalabilidad

Capacidad de un algoritmo de mantener sus prestaciones cuando aumenta el número de procesos y/o el tamaño del problema (workload).

```{dropdown} Escalabilidad

<img src="_static/images/U2_28.jpg"/>

```

- Esta característica nos permite evaluar el comportamiento del sistema cuando se incrementa el número de procesos y/o el tamaño del proceso (workload)

- Suele indicar la capacidad de una aplicación paralela para utilizar de forma eficiente un incremento en los recursos computacionales.

- Una aplicación escalable suele ser capaz de mantener su eficiencia constante cuando aumentamos el número de procesos incluso a base de aumentar el tamaño del problema (datos de entrada).

- Si un algoritmo no es escalable, aunque se aumente el número de procesos, no se conseguirá incrementar la eficiencia, con lo cual no se saca provecho de los cores del sistema


::::{grid}
:gutter: 3

:::{grid-item-card}
:class-body: text-right
:class-header: bg-light text-center
```{dropdown} Escalabilidad Fuerte
El workload es constante. El objetivo es disminuir el tiempo de ejecución de la aplicación aumentando el número de procesos.

<img src="_static/images/U2_29.jpg"/>

Está fuertemente relacionada con la ley de Amdahl (se verá a continuación).
```
:::

:::{grid-item-card}
:class-body: text-right
:class-header: bg-light text-center
```{dropdown} Escalabilidad Débil
Se aumenta el número de procesos de la aplicación manteniendo el tamaño del problema para cada proceso constante, consiguiendo que el tiempo sea constante.

<img src="_static/images/U2_30.jpg"/>

Se desprende de las observaciones de la ley de Gustafson (se verá a continuación).
```
:::

::::

## Ley de Amdahl y Ley de Gustafson

### Ley de Amdahl
Evalúa la máxima eficiencia que un algoritmo paralelo puede lograr con respecto a su versión serie.
La ecuación $S_p(n)$ se define de la siguiente manera:

$$
S_p(n) = \frac{1}{{f + \frac{{1 - f}}{p}}} \leq \frac{1}{f}
$$

Donde:
- $S_p(n)$ es la eficiencia de ejecución con $n$ procesadores.
- $f$ es el porcentaje de código no paralelizable (en decimales).
- $p$ es el número de procesadores.

```{dropdown} Ley de Amdahl

<img src="_static/images/U2_26.jpg"/>

1. **Eficiencia y Proporción Paralelizable:**
   - La eficiencia está ligada a la proporción paralelizable de un algoritmo.
   - No depende de la cantidad de procesos utilizados en el cálculo.

2. **Ley de Amdahl:**
   - Formulada por Gene Amdahl, esta ley establece que la mejora en el rendimiento de un sistema está limitada por el tiempo que se utiliza un componente específico.
   - Identificar y reducir la fracción de código no paralelizable es crucial para mejorar el rendimiento de sistemas paralelos.

3. **Identificación de Cuellos de Botella:**
   - El aumento del rendimiento en sistemas se relaciona con la identificación de los cuellos de botella.
   - Mejorar la fracción de código no paralelizable es clave para aumentar la eficiencia.

4. **Valor de la Mejora:**
   - La Ley de Amdahl ayuda a determinar si una mejora en el sistema es significativa o no.

5. **Simplificación y Limitaciones:**
   - Es un modelo simplificado de la realidad y no considera factores como el overhead de comunicación y sincronización.
   - A pesar de sus limitaciones, sigue siendo una herramienta valiosa para comprender el rendimiento y la escalabilidad.

```

:::{note}
Importante revisar el Ejercicio de esta sección
:::

### Ley de Gustafson
Establece que cualquier problema suficientemente grande puede ser eficientemente paralelizado, ofrece un nuevo punto de vista y así una visión positiva de las ventajas del procesamiento paralelo.
La ecuación $s$ se define de la siguiente manera:

$$
s = f + N(1 - f) = N - (N - 1)f
$$

Donde:
- $f$ es el porcentaje en decimales de la parte secuencial.
- $N$ es la cantidad de procesadores.

```{dropdown} Ley de Gustafson
Gustafson consideraba que  la ley de amdahl daba un límite para el descenso del tiempo de ejecución del algoritmo paralelo, dependiendo la fracción serie del algoritmo.

<img src="_static/images/U2_27.jpg"/>

Sugiere que el tamaño del problema (N) aumenta a medida que se agregan más recursos, lo que significa que la fracción del código que no se puede paralelizar se vuelve menos importante. Por lo tanto, si se puede paralelizar una gran parte del código, la aceleración obtenida aumentará en consecuencia.

```


## Ley de Moore y Ley de Huang

### Ley de Moore

La Ley de Moore, formulada por Gordon Moore en 1965 como una predicción empírica inicialmente válida por 10 años, sigue siendo una tendencia notable en la tecnología. 

```{dropdown} Ley de Moore
Aunque no es una ley universal, ha sido utilizada para describir el crecimiento exponencial de la capacidad de procesamiento y almacenamiento en dispositivos electrónicos. 

<img src="_static/images/U2_31.jpg"/>

```

La idea central es que al aumentar la cantidad de transistores en un chip, se logra un incremento en la potencia y eficiencia de los dispositivos. Aunque inicialmente predijo un duplicado anual de transistores, en realidad se cumplió aproximadamente cada dos años.

### Ley de Huang
* Sugiere que la velocidad de procesamiento puede aumentar proporcionalmente con el número de procesadores, pero solo hasta cierto punto.

* No busca sustituir a la ley de Moore.

* Cambio de paradigma en la computación. Buscan algoritmos que se sustenten en la paralelización de los datos. (La naturaleza del DL)

```{dropdown} Ley de Huang

<img src="_static/images/U2_32.jpg"/>

```

Es importante tener en cuenta la eficiencia límite al diseñar sistemas paralelos para garantizar que se utilicen los recursos adecuados y se logre el máximo rendimiento posible.


```{tip}
<a href="https://www.youtube.com/watch?v=Jlbxj182bhg" target="_blank">¿La Ley de HUANG es la nueva Ley de Moore? | Data Coffee #14</a>
```

## Precisión Simple Vs Precisión Doble y TFlops
