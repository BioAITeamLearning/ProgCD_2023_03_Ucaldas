---
title: Unidad 8
---
# Unidad 8: Multiprocessing

## Contenido de la unidad

<img src="_static/images/contenidoU8b.png"/>

## Definición de multiprocessing
- Multiprocessing es una técnica utilizada en programación para dividir un programa en varios procesos independientes que se ejecutan en paralelo en un procesador con múltiples núcleos. 

- Cada proceso tiene su propia memoria y se ejecuta de forma independiente, lo que permite una mayor eficiencia y rendimiento en la ejecución del programa.

```{dropdown} Representación gráfica
<img src="_static/images/U8_1.png"/>
```

## Multiprocessing versus Threading
A diferencia de Threading, que utiliza hilos para dividir la tarea en diferentes subprocesos, Multiprocessing utiliza procesos que se ejecutan en núcleos de procesador separados, lo que permite una verdadera ejecución en paralelo.

::::{grid}
:gutter: 3

:::{grid-item-card}
:class-body: text-right
:class-header: bg-light text-center
```{dropdown} Multiprocessing

<img src="_static/images/U8_2.png"/>

```
:::

:::{grid-item-card}
:class-body: text-right
:class-header: bg-light text-center
```{dropdown} Multithreading

<img src="_static/images/U8_3.png"/>

```
:::

::::

## Ventajas y Desventajas

### Ventajas
```{dropdown} 1. Mayor eficiencia y rendimiento
Multiprocessing permite la ejecución de varias tareas en paralelo, lo que acelera el procesamiento del programa y mejora su rendimiento.
```

```{dropdown} 2. Mayor capacidad de procesamiento
Los procesos se ejecutan en núcleos de procesador separados, lo que significa que el programa puede aprovechar completamente el potencial de la CPU para mejorar su capacidad de procesamiento.
```

```{dropdown} 3. Mayor estabilidad del programa
Los procesos se ejecutan de forma independiente, lo que significa que si un proceso falla, los demás pueden seguir ejecutándose sin problemas.
```

```{dropdown} 4. Mayor facilidad para la gestión de recursos
Multiprocessing gestiona los recursos del sistema de forma más efectiva, lo que significa que los programas pueden ser más eficientes en términos de memoria y uso de la CPU.
```

### Desventajas

```{dropdown} 1. Mayor consumo de recursos
La creación de procesos adicionales puede consumir más memoria y recursos del sistema, lo que puede afectar el rendimiento del programa.
```

```{dropdown} 2. Mayor complejidad del código
El uso de Multiprocessing puede requerir una mayor complejidad del código, lo que significa que el programa puede ser más difícil de entender y mantener.
```

```{dropdown} 3. Problemas de sincronización
La sincronización entre procesos puede ser un problema en Multiprocessing, lo que puede generar errores en el programa.
```

```{dropdown} 4. Problemas de comunicación
La comunicación entre procesos puede ser más compleja en Multiprocessing, lo que puede generar problemas de compatibilidad y de rendimiento.
```

## Programación - paso a paso
- ¿Cómo ejecutar funciones en paralelo utilizando la librería multiprocessing de Python?

```{note}
**Veamos cómo se programa**

Ver el Notebook "1 - Multiprocessing.ipynb"

```

- ¿Cómo asignar y obtener los nombres de los procesos?
```{note}
**Veamos cómo se programa**

Ver el Notebook "2 - Multiprocessing.ipynb"

```

- ¿Cómo ejecutar un proceso en segundo plano?

```{note}
**Veamos cómo se programa**

- Ver el Notebook "3 - Multiprocessing.ipynb"
- Ver el Python "3ejecutar_proceso_segundo_plano.py"

```

- ¿Cómo matar un proceso?

```{note}
**Veamos cómo se programa**

Ver el Notebook "4 - Multiprocessing.ipynb"

```

- ¿Cómo usar un proceso en una subclase?

```{note}
**Veamos cómo se programa**

Ver el Notebook "5 - Multiprocessing.ipynb"

```

- ¿Cómo intercambiar objetos entre procesos utilizando una cola?

```{note}
**Veamos cómo se programa**

Ver el Notebook "6 - Multiprocessing.ipynb"

```

- ¿Cómo intercambiar objetos entre procesos utilizando una tubería?

```{note}
**Veamos cómo se programa**

Ver el Notebook "7 - Multiprocessing.ipynb"

```

- ¿Cómo sincronizar procesos?

```{note}
**Veamos cómo se programa**

- Ver el Notebook "8 - Multiprocessing.ipynb"
- Ver el Python "8sincronizar_procesos_barrier.py"

```

- ¿Cómo sincronizar procesos utilizando un administrador de procesos (manager)?

```{note}
**Veamos cómo se programa**

Ver el Notebook "9 - Multiprocessing.ipynb"

```

- ¿Cómo ejecutar funciones en paralelo utilizando procesos con Pool?

```{note}
**Veamos cómo se programa**

Ver el Notebook "10 - Multiprocessing.ipynb"

```

## Programación - unificado

```{tip}
<a href="https://drive.google.com/file/d/1q7-BDAdjASrfu7T-4K1XlrXU0DOSnqsF/view?usp=sharing" target="_blank">Acceder a Todo en uno</a>

O ver el Notebook "Multiprocessing.ipynb"

```

```{tip}
<a href="https://drive.google.com/drive/folders/1fKro2hit0wf9R7FKUhbjc28uoK4yFFuI?usp=sharing" target="_blank">Acceder a Jupyter files</a>
```

```{tip}
<a href="https://drive.google.com/drive/folders/1A9hBa-Y3RGE50ZrSguDQNc3xz_IJQjo8?usp=sharing" target="_blank">Acceder a Python files</a>
```

## Taller y Quiz

```{tip}
Ver la subsección **Evaluemos lo aprendido!!**
```
