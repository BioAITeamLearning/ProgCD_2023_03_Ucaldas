# ¿Cómo matar un proceso?

import multiprocessing
import time

def foo():
    print ('Inicio función')
    time.sleep(1)
    print ('Final función')

if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print ('Proceso antes ejecución:', p, p.is_alive())
    
    p.start()
    print ('Proceso ejecutandose:', p, p.is_alive())
    
    p.terminate()
    print ('Proceso terminado:', p, p.is_alive())

    time.sleep(1)
    print ('Proceso terminado 1 segundo:', p, p.is_alive())

    print ('Código de salida del proceso:', p.exitcode)

# El método is_alive() del objeto Process devuelve True si el proceso está en ejecución.
# El proceso se puede matar utilizando el método terminate() del objeto Process.
# El método terminate() envía una señal SIGTERM al proceso.
# El método exitcode del objeto Process devuelve el código de salida del proceso.
# Código de salida del proceso: 
## == 0: Esto significa que no se produjo ningún error
##  > 0: Esto significa que el proceso tuvo un error y salió de ese código
##  < 0: Esto significa que el proceso se eliminó con una señal de -1 * ExitCode