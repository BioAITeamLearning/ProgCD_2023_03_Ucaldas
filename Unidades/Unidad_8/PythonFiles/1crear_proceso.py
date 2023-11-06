# ¿Cómo ejecutar funciones en paralelo utilizando la librería multiprocessing de Python?

import multiprocessing

def mi_fun(i):
    print ('Función llamada en el proceso: %s' %i)
    return

if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=mi_fun, args=(i,))
        Process_jobs.append(p)
        p.start()
    for p in Process_jobs:
        p.join()

# La librería multiprocessing de Python permite ejecutar funciones en paralelo utilizando procesos.
# Para ello, se utiliza la función Process() de la librería multiprocessing.
# La función Process() recibe como argumentos el nombre de la función que se desea ejecutar y los argumentos de la función.
# La función Process() devuelve un objeto de tipo Process que se puede almacenar en una lista.
# Para ejecutar la función, se utiliza el método start() del objeto Process.
# Para esperar a que termine la ejecución de la función, se utiliza el método join() del objeto Process.
# En el ejemplo, se crea una función mi_fun que imprime el número del proceso en el que se ejecuta.
# Se crea una lista Process_jobs que almacena los objetos Process.
# Se crea un bucle for que crea 5 procesos, los almacena en la lista Process_jobs, y los ejecuta.
# Se crea un bucle for que espera a que terminen los procesos almacenados en la lista Process_jobs.