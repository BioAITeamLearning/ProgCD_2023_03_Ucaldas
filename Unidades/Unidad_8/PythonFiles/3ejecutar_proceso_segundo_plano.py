# ¿Cómo ejecutar un proceso en segundo plano?

import multiprocessing
import time

def foo():
    name = multiprocessing.current_process().name
    print ("Inicio del proceso llamado %s" %name)
    time.sleep(2)
    print ("Final del proceso llamado %s" %name)
def foo2():
    name = multiprocessing.current_process().name
    print ("Inicio del proceso llamado %s" %name)
    time.sleep(10)
    print ("Final del proceso llamado %s" %name)

if __name__ == '__main__':
    background_process = multiprocessing.Process(name='background_process',target=foo2)
    background_process.daemon = True

    NO_background_process = multiprocessing.Process(name='NO_background_process',target=foo)    
    NO_background_process.daemon = False
    
    background_process.start()
    NO_background_process.start()
    #background_process.join()
    #NO_background_process.join() 
    print ("Final del principal") 
    
# Los procesos en el modo NO_background_process tienen una salida, por lo que el proceso demoníaco 
# finaliza automáticamente después de que finaliza el programa principal para evitar la persistencia
# de los procesos en ejecución.