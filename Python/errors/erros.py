"""SintaxError"""
## Los errores de sintaxis, también conocidos como errores de interpretación

# while True print("Hello")

# -> print("hello"

# -> print("hello)

# -> deF func(): pass

"""AssertionError"""
# Se genera cuando se produce un error en una instrucción assert.

has_connection: bool = False 

# -> assert has_connection, "No connection..."

"""AttributeError""" 
## Se genera cuando se produce un error en una referencia de atributo  o la asignación falla. 

number = 10
# -> number.append(10)

class Apple:
    ...

apple = Apple()
# -> apple.run()


"""ImportError"""
## Se genera cuando la instrucción import tiene problemas al intentar cargar un módulo. También se produce cuando la from list en from ... import tiene un nombre que no se puede encontrar.

# -> from PIL import tab

"""ModuleNotFoundError"""
## Una subclase de ImportError que se genera mediante import cuando no se pudo encontrar un módulo. También se genera cuando None se encuentra en sys.modules.

# -> import subscribe

"""IndexError"""
## Se genera cuando un subíndice de secuencia está fuera del rango.

lista = [1,2,3,4.5]

# -> lista[6]

"""KeyError"""
## Se genera cuando no se encuentra una clave de asignación (diccionario) en el conjunto de claves existentes (mapa).

dicc = {"a": 1, "b": 2, "c": 3}

# -> dicc["d"]

"""KeyboardInterrupt"""
## Se genera cuando el usuario pulsa la tecla de interrupción (normalmente Control-C o Delete). Durante la ejecución, se realiza una comprobación de interrupciones con regularidad.


"""NameError"""
## Se genera cuando no se encuentra un nombre local o global. Esto se aplica solo a nombres no calificados. El valor asociado es un mensaje de error que incluye el nombre que no se pudo encontrar.

# -> print(name) 


"""RecursionError"""
##  Esta excepción se deriva de RuntimeError. Se lanza cuando el intérprete detecta que se excede la profundidad máxima de recursión (ver sys.getrecursionlimit()).

def func():
    func()

# -> func()

"""IndentationError"""
# Clase base para errores de sintaxis relacionados con sangría incorrecta.
 
# ->  a


"""TypeError"""
##  Se genera cuando una operación o función se aplica a un objeto de tipo inapropiado. El valor asociado es una cadena que proporciona detalles sobre la falta de coincidencia de tipos.

# -> print("Hello" + 10)


"""ValueError"""
## Se genera cuando una operación o función recibe un argumento que tiene el tipo correcto pero un valor inapropiado, y la situación no se describe con una excepción más precisa como IndexError.

# -> number = int("Hello")

"""StopIteration"""
## Generado por la función incorporada next() y un iterator's __next__() para indicar que no hay más elementos producidos por el iterador. 

x = iter([1,2,3])

for i in range(4):
    # -> print(next(x))
    pass


"""FileNotFoundError"""
# Raised when a file or directory is requested but doesn’t exist.

# -> f = open("test.txt")

