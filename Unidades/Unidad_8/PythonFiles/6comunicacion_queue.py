# ¿Cómo intercambiar objetos entre procesos utilizando una cola?

import multiprocessing
import random
import time

class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self) :
        for i in range(5):
            item = random.randint(0, 256)
            self.queue.put(item) 
            print ("Proceso Producer: item %d agregado a la cola %s" % (item,self.name))
            time.sleep(0.5)
            print ("El tamaño de la cola es %s" % self.queue.qsize())
       
class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("La cola está vacía")
                break
            else :
                time.sleep(1)
                item = self.queue.get()
                print ('Proceso Consumer: item %d sacado de %s \n' % (item, self.name))
                time.sleep(0.5)

if __name__ == '__main__':
        queue = multiprocessing.Queue()
        process_producer = producer(queue)
        process_consumer = consumer(queue)
        process_producer.start()
        process_consumer.start()
        process_producer.join()
        process_consumer.join()

# La librería multiprocessing de Python permite intercambiar objetos entre procesos utilizando una cola.
# Para ello, se utiliza la clase Queue() de la librería multiprocessing.
# La clase Queue() recibe como argumento el tamaño máximo de la cola.
# La clase Queue() tiene los métodos put() y get() para añadir y obtener objetos de la cola.
# En el ejemplo, se crea una clase producer que hereda de la clase Process de la librería multiprocessing.
# La clase producer sobreescribe el método run() de la clase Process.
# La clase producer añade objetos a la cola utilizando el método put() de la clase Queue.
# La clase producer imprime el tamaño de la cola utilizando el método qsize() de la clase Queue.
# Se crea una clase consumer que hereda de la clase Process de la librería multiprocessing.
# La clase consumer sobreescribe el método run() de la clase Process.
# La clase consumer obtiene objetos de la cola utilizando el método get() de la clase Queue.
# La clase consumer imprime los objetos obtenidos de la cola.
# La clase consumer imprime un mensaje si la cola está vacía.