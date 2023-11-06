# ¿Cómo asignar y obtener los nombres de los procesos?

import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Inicio del proceso llamado %s" %name)
    time.sleep(2)
    print ("Final del proceso llamado %s" %name)

if __name__ == '__main__':
    process_with_default_name1 = multiprocessing.Process(target=foo)
    process_with_default_name2 = multiprocessing.Process(target=foo)
    process_with_name = multiprocessing.Process(name='foo_process',target=foo)
    process_with_name.start()
    process_with_default_name1.start()
    process_with_default_name2.start()
    
# El nombre del proceso se puede obtener utilizando la función current_process() de la librería multiprocessing.
# El nombre del proceso se puede asignar utilizando el argumento name de la función Process() de la librería multiprocessing.