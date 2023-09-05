import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

last_build_time = 0
DEBOUNCE_TIME = 7  # tiempo en segundos

# Función para construir el libro Jupyter Book
def build_book():
    global last_build_time

    current_time = time.time()
    if current_time - last_build_time < DEBOUNCE_TIME:
        print("Debouncing build")
        return

    print("Building the Jupyter Book...")
    subprocess.run(["jupyter-book", "build", "./"])
    print("Build complete!")

    last_build_time = current_time

# Clase para manejar eventos de sistema de archivos
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory or not event.src_path.endswith(".md"):
            return
        build_book()

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()

    # Observar el directorio actual y sus subdirectorios de forma recursiva
    observer.schedule(event_handler, path="./", recursive=True)
    observer.start()
    
    try:
        # Ejecutar en bucle hasta que se interrumpa con Ctrl+C
        while True:
            time.sleep(1)  # Reducir el tiempo de espera para una respuesta más rápida
    except KeyboardInterrupt:
        # Detener el observador y esperar a que termine
        observer.stop()
    observer.join()
