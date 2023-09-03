---
title: Unidad 2
---
# Unidad 2: Arquitecturas para computación paralela

## Contenido de la unidad

<img src="images/contenidoU2.png"/>

---

## Arquitectura de memoria en computación paralela
### Taxonomía de Flynn

<img src="images/U2_1.jpg"/>

* **SISD**: El procesador ejecuta una única instrucción en una única pieza de datos en cada ciclo de reloj. - Ordenador.

* **MISD**: Múltiples procesadores ejecutan diferentes instrucciones en el mismo conjunto de datos. Un ejemplo de un sistema MISD es un sistema de detección de fallas de seguridad en tiempo real, en el que varias instrucciones de verificación se ejecutan simultáneamente en la misma pieza de datos para detectar cualquier falla.

* **SIMD**: En este caso, el procesador ejecuta la misma instrucción en varios datos diferentes en cada ciclo de reloj - GPU

* **MIMD**: Múltiples procesadores ejecutan diferentes instrucciones en diferentes conjuntos de datos al mismo tiempo. clúster de servidores que ejecutan aplicaciones separadas en cada servidor, pero se comunican entre sí para realizar una tarea común.

---

```{dropdown} SISD

En un ciclo del reloj:

<img src="images/U2_2.jpg"/>
<img src="images/U2_3.jpg"/>

#### Ejemplo
<img src="images/U2_4.jpg"/>

```

```{dropdown} MISD

Poco práctico comercialmente

<img src="images/U2_5.jpg"/>

```

```{dropdown} SIMD

En este se basa la arquitectura de la GPU

<img src="images/U2_6.jpg"/>

#### Ejemplo
<img src="images/U2_7.jpg"/>

```

```{dropdown} MIMD

* Arquitectura aplicada en supercomputadores. 
* Async algorithms

<img src="images/U2_8.jpg"/>

#### Ejemplo
<img src="images/U2_9.jpg"/>

```

---
## Organización de la memoria

En la arquitectura MIMD

<img src="images/U2_10.jpg"/>

### Memoria Compartida
Misma memoria para todos los procesadores.

<img src="images/U2_11.jpg"/>

#### Tipos de acceso a memoria en memoria compartida

* Acceso uniforme a la memoria (UMA)

<img src="images/U2_12.jpg"/>

* Acceso no-uniforme a la memoria (NUMA)

<img src="images/U2_13.jpg"/>

* Sin acceso remoto a la memoria (NORMA)

* Acceso solo a la memoria caché (COMA)

### Memoria Distribuida: Sistemas Multicomputadores
* Small complete systems

<img src="images/U2_14.jpg"/>

* Protocolo de paso de mensajes

<img src="images/U2_15.jpg"/>

* Procesamiento masivo paralelo

Muchos procesadores, conectados por una red de comunicación.

<img src="images/U2_16.jpg"/>

* La arquitectura heterogénea

CUDA y OpenCL
<img src="images/U2_17.jpg"/>

## Modelos de programación paralela

* Existen como una abstracción de las arquitecturas de hardware

* No existe un modelo mejor que otro, depende del problema

<img src="images/U2_18.jpg"/>

### Paradigma del modelo de paso de mensajes 

El modelo MPI está diseñado con memoria distribuida, pero al ser modelos de programación paralela, también puede utilizarse en una máquina de memoria compartida.

<img src="images/U2_19.jpg"/>

### Modelo de datos paralelos
Las GPU de la generación actual operan con alta eficiencia con los datos alineados

<img src="images/U2_20.jpg"/>

## ¿Cómo diseñar un programa paralelo ?

Cuando se diseña un algoritmo es necesario tener en cuenta:

* Los tiempos de las comunicaciones

* Maximizar el procesamiento en cada nodo o unidad de procesamiento.

* Los costes de implementar el algoritmo

* Tiempos de planificación

<img src="images/U2_21.jpg"/>

### Metodología foster para diseño
Consiste en cuatro etapas:

<img src="images/U2_22.jpg"/>
