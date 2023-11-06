# ¿Cómo usar un proceso en una subclase? 

import multiprocessing

class MyProcess(multiprocessing.Process):

    def run(self):
        print ('called run method in %s' %self.name)
        return

if __name__ == '__main__':
    jobs = []

    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()

    for p in jobs:        
        p.join()

# La librería multiprocessing de Python permite crear procesos utilizando subclases.
# Para ello, se crea una clase que hereda de la clase Process de la librería multiprocessing.
# En el ejemplo, se crea una clase MyProcess que hereda de la clase Process.
# La clase MyProcess sobreescribe el método run() de la clase Process.
# La clase MyProcess llama al método run() de la clase Process.
# Se crea una lista jobs que almacena los objetos MyProcess.
# Se crea un bucle for que crea 5 procesos, los almacena en la lista jobs, y los ejecuta.
# Se crea un bucle for que espera a que terminen los procesos almacenados en la lista jobs.