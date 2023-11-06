# ¿Cómo sincronizar procesos?

import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    
    with serializer:
        print("Proceso %s ----> %s" %(name,datetime.fromtimestamp(now)))

    #serializer.acquire()
    #print("Proceso %s ----> %s" %(name,datetime.fromtimestamp(now)))
    #serializer.release()

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("Proceso %s ----> %s" %(name ,datetime.fromtimestamp(now)))

if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='p1 - prueba_con_barrera',target=test_with_barrier,args=(synchronizer,serializer)).start()
    Process(name='p2 - prueba_con_barrera',target=test_with_barrier,args=(synchronizer,serializer)).start()
    Process(name='p3 - prueba_sin_barrera',target=test_without_barrier).start()
    Process(name='p4 - prueba_sin_barrera',target=test_without_barrier).start()
    
# La sincronización de procesos se puede lograr utilizando la clase Barrier de la librería multiprocessing.
# La sincronización de procesos se puede lograr utilizando la clase Lock de la librería multiprocessing.