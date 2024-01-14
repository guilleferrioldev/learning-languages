# En programación, una closure (clausura o cierre) es una función que se "recuerda" y mantiene el entorno en el que fue creada, incluso cuando la función se utiliza fuera de ese entorno. En otras palabras, una closure es una función junto con su entorno léxico.

# En Python, las closures se crean cuando una función interna hace referencia o utiliza variables de una función externa. La función interna puede acceder y "recordar" las variables de la función externa, incluso después de que la función externa haya finalizado su ejecución.

# Un decorador es una funcion que toma otra funcion como argumento y devuelve una funcion.

# Un decorador es una función especial en Python que se utiliza para modificar o envolver otra función sin alterar su implementación original. Es una forma elegante y poderosa de extender o personalizar el comportamiento de una función sin tener que modificar su código fuente.

# Un decorador puede realizar diversas tareas, como agregar registro de eventos, validar argumentos, realizar transformaciones en los datos de entrada o salida, manejar excepciones y más. Proporciona una forma modular y reutilizable de agregar funcionalidad adicional a las funciones.

# La función wraps del módulo functools en Python se utiliza para crear decoradores que preservan los metadatos de las funciones decoradas. 
# Cuando decoras una función con otro función (decorador), la función decoradora reemplaza a la original, lo que significa que los metadatos como el nombre de la función, la documentación y los argumentos se pierden. El uso de wraps ayuda a solucionar este problema.
# Al decorar una función con wraps, se copian los atributos importantes de la función original a la función decorada, lo que permite que la función decorada retenga su identidad y metadatos.
from functools import wraps


"""Closures"""
def outer_function(msg):
    # closure 
    def inner_func(msg2):
        print(msg + " " + msg2)
    # si devolvemos la funcion ejecutada se ejecutará directamente, pero si la devolvemos sin ejecutar ella esperará a ser ejecutada.
    return inner_func

hi_func = outer_function("hi")
bye_func = outer_function("bye")
#hi_func("you")
#bye_func("name")



"""Decorators"""
### Ejemplo 1
def decorator_func(original_func):
    @wraps(original_func)
    def wrapper(*args, **kwargs):  #wrapper es envoltura
        print(f"wrapper executed the before {original_func.__name__}")
        return original_func(*args, **kwargs)

    return wrapper 

@decorator_func
def display():
    print("display function ran")

# Es lo mismo que ejecutar la funcion decorador, pasarle como argumento a display y ejecutarlo 
#display() # ==  decorator_func(display)()


### Ejemplo 2 
@decorator_func
def display_info(name, age):
    print(f"display_info ran with arguments {name}, {age}")

# display_info("Pedro", 22)



"""Classes as decorators"""
class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func
        # se utiliza para aplicar el decorador wraps al método decorador __init__ dentro de la clase. Esto asegura que los metadatos de la funcion original se copien correctamente al método decorado (__call__).
        wraps(original_func)(self)

    def __call__(self, *args, **kwargs):
        print(f"call method executed the before {self.original_func.__name__}")
        return self.original_func(*args, **kwargs)

### Ejemplo  3
@decorator_class
def display():
    print("display function ran")

#display()

# Ejemplo 4 
@decorator_class 
def display_info(name, age):
    print(f"display_info ran with arguments {name}, {age}")

#display_info("Pedro", 22)



"""Lambda decorator"""
# Invoca la funcion sin que sea llamada

from datetime import datetime 

@lambda _: _()
def func() -> None:
    time_text: str = f"Started at {datetime.now(): %H:%M:%S}"
    #print(time_text)
    return time_text 

@lambda _:_(6,7)
def mult(a, b) -> int:
    #print(a * b)
    return a * b 
