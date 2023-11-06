# ¿Cómo sincronizar procesos utilizando un administrador de procesos (manager)?

import multiprocessing
import time

def worker(dictionary, key, item):
    print(key,item)
    time.sleep(2)
    dictionary[key] = item

if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()
    jobs = [ multiprocessing.Process(target=worker, args=(dictionary, i, i*2)) for i in range(10) ]
    
    start_time = time.time()
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()

    end_time = time.time()
    print ('Results:', dictionary)

    print("El tiempo de ejecución fue:", end_time - start_time, "segundos")

# La sincronización de procesos se puede lograr utilizando un administrador de procesos (manager).    