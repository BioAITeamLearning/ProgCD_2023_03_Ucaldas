---
title: Unidad 6
---
# Unidad 6: Infraestructura de cluster

## Contenido de la unidad

<img src="_static/images/contenidoU6.png"/>

## HPC y cluster
<img src="_static/images/U6_1.jpg"/>

## Arquitectura general
<img src="_static/images/U6_2.jpg"/>

## Distribución del espacio físico
<img src="_static/images/U6_3.jpg"/>

## UPS
<img src="_static/images/U6_4.jpg"/>

## Aire acondicionado de precisión
<img src="_static/images/U6_5.jpg"/>

## Racks de servidores
<img src="_static/images/U6_6.jpg"/>

## Switches
<img src="_static/images/U6_7.jpg"/>

## Conectividad: infiniband
<img src="_static/images/U6_8.jpg"/>

```{dropdown} InfiniBand
<img src="_static/images/U6_9.jpg"/>
```
## Nodos de computo
<img src="_static/images/U6_10.jpg"/>

## Nodos de almacenamiento: nas
<img src="_static/images/U6_11.jpg"/>

## Nodos de almacenamiento: nas
<img src="_static/images/U6_12.jpg"/>

## Esquema básico disposición cluster
<img src="_static/images/U6_13.jpg"/>

## Esquema básico
<img src="_static/images/U6_14.jpg"/>

## Esquema básico: Conexión cluster
<img src="_static/images/U6_15.jpg"/>

## Conexión cluster: VPN
<img src="_static/images/U6_16.jpg"/>

## Esquema básico
<img src="_static/images/U6_17.jpg"/>

## Arquitectura cluster BIOS
<img src="_static/images/U6_18.jpg"/>

```{note}
**Análisis de los TFlops BIOS**

Ver el Excel "Cálculo de Tflops BIOS.xlsx"

```

## Arquitectura cluster BIOS
<img src="_static/images/U6_19.jpg"/>

## Arquitectura cluster BIOS-INSPUR
<img src="_static/images/U6_20.jpg"/>

```{note}
**Análisis de los TFlops BIOS-INSPUR**

Ver el Excel "Análisis de capacidades TFlops INSPUR BIOS.xlsx"

```

## Arquitectura cluster BIOS-INSPUR
<img src="_static/images/U6_21.jpg"/>

## Sistemas operativos
<img src="_static/images/U6_22.jpg"/>

## Análisis Financiero de BIOS
<img src="_static/images/U6_23.jpg"/>

## Software de cluster
- Sistema Operativo: 
    - Linux Centos.
- Administrador de colas (Job Manager): 
    - ClusterEngine HPC Professional edition.
- Plataforma de virtualización: 
    - ClusterEngine Unified Cloud Service Platform-HPC Basic Edition.

<img src="_static/images/U6_24.jpg"/>

- Librerías para ejecución de entornos en paralelo:
    - MPICH: 1Gb parallel message passing library.
    - MVAPICH2: 10Gb/IB parallel message passing library.
    - OpenMPI: high-performance message passing library.

<img src="_static/images/U6_25.jpg"/>

- Entornos de programación:
    - Intel Math Kernel Library
    - GCC compiler
    - Intel compiler & debugging software.
    - Intel C++/Fortran compiler.

<img src="_static/images/U6_26.jpg"/>

- Software para gestión de almacenamiento y acceso a datos:
    - Intel Enterprise Edition Lustre
    - Hadoop

<img src="_static/images/U6_27.jpg"/>

## Organización de directorios
<img src="_static/images/U6_28.jpg"/>

## Librerías y módulos
<img src="_static/images/U6_29.jpg"/>

## Librerías y módulos
<img src="_static/images/U6_30.jpg"/>

```{tip}
<a href="https://modules.readthedocs.io/en/latest/" target="_blank">Environment Modules — Modules documentation</a>
<img src="_static/images/U6_31.jpg"/>
```

## Paralelización en cluster: Ley de amdahl
<img src="_static/images/U6_32.jpg"/>

## Paralelización en cluster: Taxonomía Flynn

- SISD
    - La CPU procesa únicamente una instrucción por cada ciclo de reloj.
    - Únicamente un dato es procesado en cada ciclo de reloj.
    - Es el modelo más antiguo de computadora y el más extendido.

- MISD
    - Cada unidad ejecuta una instrucción distinta.
    - Cada unidad procesa el mismo dato.
    - Aplicación muy limitada en la vida real.

- SIMD
    - Todas las unidades ejecutan la misma instrucción.
    - Cada unidad procesa un dato distinto.
    - Todas las unidades operan simultáneamente.

- MIMD
    - Cada unidad ejecuta una instrucción distinta.
    - Cada unidad procesa un dato distinto.
    - Todas las unidades operan simultáneamente.

<img src="_static/images/U6_33.jpg"/>

## Paralelización en cluster: Hyper Threading
<img src="_static/images/U6_34.jpg"/>

## Tipos de paralelización: Multicore OpenMP
<img src="_static/images/U6_35.jpg"/>

## Tipos de paralelización: Multinodo MPI
<img src="_static/images/U6_36.jpg"/>

## Tipos de paralelización: MPI+OpenMP
<img src="_static/images/U6_37.jpg"/>

## Tipos de paralelización: GPU
<img src="_static/images/U6_38.jpg"/>

## Tipos de paralelización: GPU
<img src="_static/images/U6_39.jpg"/>

## Ejecución de procesos de manera general
<img src="_static/images/U6_40.jpg"/>

## Calendarizadores
<img src="_static/images/U6_41.jpg"/>

## Flujo de trabajo calendarizador
<img src="_static/images/U6_42.jpg"/>

## Capacidades en HPC
<img src="_static/images/U6_38.jpg"/>

## Proyectos ejecutados
<img src="_static/images/U6_39.jpg"/>

## Recursos Extra
```{tip}
<a href="https://upcommons.upc.edu/bitstream/handle/2099.1/15791/77790.pdf?sequence=1" target="_blank"> Instalación y configuración de un cluster de computación</a>

<a href="https://es.slideshare.net/kacjoa/diseo-y-normas-para-data-centers" target="_blank">Diseño y normas para data centers</a>
```

