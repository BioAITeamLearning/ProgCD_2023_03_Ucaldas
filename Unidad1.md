---
title: Unidad 1
---
# Unidad 1: Clusters en computación paralela/distribuida

## Contenido de la unidad

<img src="images/contenidoU1.png"/>

---

## Introducción al HPC

**HPC**: Cualquier  técnica computacional que soluciona un problema grande de forma más rápida que usando posiblemente sistemas simples.

HPC ha tenido gran impacto sobre todas las áreas de ciencias computacionales e ingenieria en la academia, gobierno e industria.

Muchos problemas han sido solucionados con técnicas de **HPC** que eran imposibles de solucionar con estaciones de trabajo individuales o computadores personales.

<img src="images/U1_1.png"/>

---

```{dropdown} Procesadores de alto rendimiento

<img src="https://hardzone.es/app/uploads-hardzone.es/2023/02/Computacion-Alto-Rendimiento-HPC-Portada.jpg"/>

```

```{dropdown} Computación paralela

Sistemas simples con varios procesadores trabajando sobre el mismo problema

<img src="https://www.tibco.com/sites/tibco/files/media_entity/2021-06/massively-parallel-processing-diagram.svg" />

#### Computación paralela Vs Computador paralelo

- Computación Paralela: el uso de múltiples computadores o procesadores trabajando en conjunto sobre una tarea común 
- Computador Paralelo: un computador que contiene múltiples procesadores:
    * Cada procesador trabaja sobre una sección del problema
    * Los procesadores permiten intercambio de información con otros procesadores

<img srcr="https://camo.githubusercontent.com/265827bf0ab59a671404f5a215363de6626c1e3284ad435fbbdf9291746d8bea/687474703a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f662f66312f466f726b5f6a6f696e2e7376672f3130343070782d466f726b5f6a6f696e2e7376672e706e67"/>


<img src="images/U1_14.png"/>

<img src="images/U1_15.png">
```

```{dropdown} Computación/programación Concurrente

<img src="images/U1_6.png"/>

la programación concurrente se enfoca en manejar múltiples tareas al mismo tiempo (ya sea simultáneamente o dando la ilusión de simultaneidad), la programación paralela se enfoca en la división y ejecución simultánea de tareas para resolver un problema más grande en menos tiempo.


```

```{dropdown} Computación Distribuida

Varios sistemas acoplados por un  secuenciador de trabajo sobre problemas relacionados

<img src="images/U1_12.png"/>

### Sistemas distribuidos

<img src="images/U1_5.png"/>
```

```{dropdown} Computación grid

<img src="images/U1_3.png"/>

Varios sistemas acoplados por software y redes para trabajar en conjunto en problemas simples o en problemas relacionados.

Unión de Clusters de computadores, recursos computacionales, datos, grupos de investigación, científicos, etc., distribuidos geográficamente y conectados mediante redes WAN

#### Funcionamiento de la computación grid
Middleware para comunicación transparente y explotación de recursos.

- El objetivo final es usar recursos remotos
- Se requieren conexiones de redes rápidas
- El grid busca el uso eficiente de los recursos
- Es escencial la seguridad centrada en: políticas de acceso, autenticación y autorización.
- Es importante estandarizar las aplicaciones grid.

<img src="images/U1_13.png"/>

<img src="images/U1_16.png"/>

#### Arquitectura Grid

* Capa de aplicación
* Capa de middleware
* Capa de recursos
* Capa de red

##### Middleware
El autentico cerebro del grid, se encarga de las siguientes funciones:

* Encontrar lugar conveniente para ejecutar la tarea solicitada por el usuario
* optimizar el uso de recursos que se encuentren dispersos
* organizar el acceso eficiente a los datos
* autenticar los diferentes elementos
* ejecutar tareas
* monitorizar el progreso de los trabajos en ejecución
* gestionar automáticamente la recuperación frente a fallos
* Notificar el fallo, culminación de la ejecución de una tarea y sus resultados.

<img src="images/U1_17.png"/>

```

---
## ¿Dónde corre lo que se va a programar en el curso?
### Infraestructura: Cluster

<img src="images/U1_2.png"/>

### Colas y calendarizadores

<img src="images/U1_20.png"/>

* Administrar recursos del Clúster
* Priorizar trabajos
* Limitar capacidad de cómputo
* Administrar usuarios

---

<img src="images/U1_21.png"/>

<img src="images/U1_22.png"/>

#### Algunos calendarizadores

<img src="images/U1_23.png"/>

---

#### Flujo de trabajo con calendarizadores

<img src="images/U1_24.png"/>

---
#### Así se ve un job para calendarizador

<img src="images/U1_25.png"/>

### Infraestructura: Cloud

<img src="images/U1_4.png"/>

- Externalizar TI a proveedores de servicio
- Presentar transparencia al usuario final
- Asignación dinámica de recursos bajo demanda (Sin compartir) – Pago asociado
- Virtualización

### Computación cloud

<img src="images/U1_18.png"/>

### Infraestructura tradicional Vs Cloud

<img src="images/U1_19.png"/>

---



## CPU & GPU & TPU

<img src="images/U1_7.png"/>
<img src="images/U1_9.png">

---

## CPU & GPU

<img src="images/U1_8.png"/>

---

## Actualidad del software para Big Data

<img src="images/U1_10.png">

---
## Aplicaciones del HPC

<img src="images/U1_11.png"/>