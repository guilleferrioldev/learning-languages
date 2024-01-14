# El currying es una técnica en programación funcional que consiste en convertir una función que toma varios argumentos en una secuencia de funciones que toman un solo argumento. El nombre "currying" se debe al matemático y lógico Haskell Curry, quien fue uno de los primeros en estudiar esta técnica. 

# Cuando se aplica el currying a una función, se crea una nueva función cada vez que se le pasa un argumento parcial. Esta nueva función toma el siguiente argumento y devuelve otra función hasta que se proporcionen todos los argumentos necesarios. Una vez que se proporcionan todos los argumentos, se ejecuta la función original.

# El currying puede ser útil en situaciones donde queremos utilizar argumentos parciales para reutilizar lógica o crear funciones más especializadas a partir de una función más general. También puede facilitar la composición de funciones en la programación funcional.


from typing import Callable

def multiply_setup(amount: float) -> Callable:
    def multiply(number: float) -> float:
        return amount * number
    
    return multiply 


# Es la misma función
def multiply_lambda(amount: float) -> Callable:
    return lambda number: amount * number


# Los decoradores son ejemplos de curring
def multiplicador(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * n
        return wrapper
    return decorator

@multiplicador(3)
def suma(a, b):
    return a + b 


x = multiply_setup(2)(10)
double = multiply_lambda(2)
suma = suma(2,3) 

print(x)
print(double(10))
print(suma)
