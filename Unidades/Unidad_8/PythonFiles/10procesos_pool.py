# ¿Cómo ejecutar funciones en paralelo utilizando procesos con Pool?

import multiprocessing

def function_square(data):
    result = data*data
    return result

if __name__ == '__main__':
    inputs = list(range(0,100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)

    pool.close() 
    pool.join()  
    print ('Pool    :', pool_outputs)

# La función Pool() recibe como argumento el número de procesos que se desea crear.
# Para ejecutar la función, se utiliza el método map() del objeto Pool.
# Para esperar a que terminen la ejecución de las funciones, se utiliza el método close() y el método join() del objeto Pool.

# Cuando se crea la instancia de multiprocessing.Pool con processes=4, se están creando 4 procesos en paralelo 
# para ejecutar la función function_square en cada uno de ellos, utilizando los elementos de la lista inputs como entrada. 
# Cada proceso recibe un subconjunto de los datos y ejecuta la función sobre ellos de manera independiente y 
# concurrente con los otros procesos. 
# Al final, se recopilan los resultados y se devuelven como una lista en el orden en que se completaron.