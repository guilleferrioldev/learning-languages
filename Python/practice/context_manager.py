import json

class JSONFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path)
        return json.load(self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f"Se produjo una excepción: {exc_type}, {exc_val}")
            # Puedes optar por relanzar la excepción si es necesario
            # raise exc_type(exc_val)

# Ejemplo de uso del context manager para abrir un archivo JSON
file_path = "data.json"
with JSONFileReader(file_path) as data:
    print(f"Contenido del archivo JSON '{file_path}':")
    print(data)
    # Realiza acciones adicionales con los datos del archivo JSON

print("Fuera del bloque 'with'")