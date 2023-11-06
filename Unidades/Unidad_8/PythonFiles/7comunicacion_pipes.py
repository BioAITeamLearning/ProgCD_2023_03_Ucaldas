# ¿Cómo intercambiar objetos entre procesos utilizando una tubería?

import multiprocessing 

def create_items(pipe):
    output_pipe, _ = pipe
    for item in range(10):
        output_pipe.send(item)
    output_pipe.close()

def multiply_items(pipe_1, pipe_2):
    close, input_pipe = pipe_1
    close.close()
    output_pipe, _ = pipe_2
    try:
        while True:
            item = input_pipe.recv()
            output_pipe.send(item * item)
    except EOFError:
        output_pipe.close()

if __name__== '__main__':
    pipe_1 = multiprocessing.Pipe(True)
    process_pipe_1 = multiprocessing.Process(target=create_items, args=(pipe_1,))
    process_pipe_1.start()

    pipe_2 = multiprocessing.Pipe(True)
    process_pipe_2 = multiprocessing.Process(target=multiply_items, args=(pipe_1, pipe_2,))
    process_pipe_2.start()
 
    pipe_1[0].close()
    pipe_2[0].close()

    try:
        while True:            
            print(pipe_2[1].recv())
    except EOFError:
        print ("End")

# La librería multiprocessing de Python permite intercambiar objetos entre procesos utilizando una tubería.
# Para ello, se utiliza la clase Pipe() de la librería multiprocessing.
# La clase Pipe() tiene los métodos send() y recv() para añadir y obtener objetos de la tubería.
# Después de iniciar los procesos y establecer las tuberías entre ellos, se cierran los extremos de lectura de pipe_1 y pipe_2 
# en el proceso principal usando pipe_1[0].close() y pipe_2[0].close(). 
# Esto se hace para indicar que el proceso principal ya no está utilizando los extremos de lectura de las 
# tuberías y para que los procesos secundarios puedan continuar funcionando sin interrupciones.
# Luego, se utiliza un bucle try-except para recibir los objetos enviados por el proceso secundario a través de pipe_2. 
# El bucle continúa hasta que se produce un EOFError, lo que indica que ya no hay más objetos en la tubería. 
# En cada iteración del bucle, se llama a pipe_2[1].recv() para recibir el objeto enviado por el proceso secundario
# y se imprime en la consola usando print(). 