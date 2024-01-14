from functools import cache , cached_property, lru_cache, partial, partialmethod, singledispatch, singledispatchmethod, update_wrapper, wraps, total_ordering

"""cache--------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Caché de funciones ilimitado, ligero y simple. Aveces llamado «memoización».

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

"""cached_property----------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Transforma un método de una clase en una propiedad cuyo valor se computa una vez y luego se almacena como un atributo normal durante la vida de la instancia. Similar a property(), con la adición de caching. Útil para propiedades calculadas costosas de instancias que de otra manera son efectivamente inmutables.

class DataSet:
    def __init__(self, sequence_of_numbers):
        self._data = tuple(sequence_of_numbers)

    @cached_property
    def stdev(self):
        return statistics.stdev(self._data)

"""lru_cache----------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Decorador para envolver una función con un memorizador invocable que guarda hasta el maxsize de las llamadas más recientes. Puede salvar el tiempo cuando una función costosa o de E/S es llamada periódicamente con los mismos argumentos.

@lru_cache
def count_vowels(sentence):
    return sum(sentence.count(vowel) for vowel in 'AEIOUaeiou')

@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# Si maxsize está configurado como None, la función LRU está desactivada y la caché puede crecer sin límites.

# Si typed se establece en verdadero, los argumentos de función de diferentes tipos se almacenarán en caché por separado. Si typed es falso, la implementación generalmente las considerará como llamadas equivalentes y solo almacenará en caché un único resultado. (Algunos tipos como str y int pueden almacenarse en caché por separado incluso cuando typed es falso).

# La función envuelta está instrumentada con una función cache_parameters() que retorna un nuevo dict que muestra los valores para maxsize y typed. Esto es solo para fines informativos. La mutación de los valores no tiene ningún efecto.
parameters = fib.cache_parameters()

# Para ayudar a medir la efectividad de la caché y afinar el parámetro maxsize, la función envolvente está instrumentada con una función cache_info() que retorna un named tuple mostrando hits, misses, maxsize y currsize.
info = fib.cache_info()

# El decorador también proporciona una función cache_clear() para limpiar o invalidar la caché.

"""total_ordering----------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Dada una clase que define uno o más métodos de ordenamiento de comparación ricos, este decorador de clase suministra el resto. Esto simplifica el esfuerzo de especificar todas las posibles operaciones de comparación rica:

# La clase debe definir uno de __lt__(), __le__(), __gt__(), o __ge__(). Además, la clase debe suministrar un método __eq__(). Dada una clase que define uno o más métodos de ordenamiento de comparación ricos, este decorador de clase suministra el resto. Esto simplifica el esfuerzo de especificar todas las posibles operaciones de comparación rica.

@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))


"""partial------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# El partial() se utiliza para la aplicación de funciones parciales que «congela» (freezes) alguna porción de los argumentos y/o palabras clave de una función dando como resultado un nuevo objeto con una firma simplificada. Por ejemplo, partial() puede usarse para crear una llamada que se comporte como la función int() donde el argumento base tiene un valor por defecto de dos:

basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
b2 = basetwo('10010')


"""partialmethod-----------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Retorna un nuevo descriptor partialmethod que se comporta como partial excepto que está diseñado para ser usado como una definición de método en lugar de ser directamente invocable.
# Cuando func es una llamada no descriptiva, se crea dinámicamente un método de unión apropiado. Esto se comporta como una función Python normal cuando se usa como método: el argumento self se insertará como el primer argumento posicional, incluso antes de las args y keywords suministradas al constructor partialmethod.

class Cell:
    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)

c = Cell()
#print(c.alive)
c.set_alive()
#print(c.alive)


"""singledispatch----------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Transformar una función en una single-dispatch generic function.

# Para definir una función genérica, decórala con el decorador @singledispatch. Al definir una función usando @singledispatch, tenga en cuenta que el envío ocurre en el tipo del primer argumento

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)

# Para agregar implementaciones sobrecargadas a la función, use el atributo register() de la función genérica, que se puede usar como decorador. Para las funciones anotadas con tipos, el decorador inferirá automáticamente el tipo del primer argumento:

@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


"""singledispatchmethod----------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Transformar un método en un single-dispatch generic function.

# Para definir un método genérico, decóralo con el decorador @singledispatchmethod. Al definir una función usando @singledispatchmethod, tenga en cuenta que el envío ocurre en el tipo del primer argumento no self o no cls:

# @singledispatchmethod admite la anidación con otros decoradores como @classmethod. Tenga en cuenta que para permitir dispatcher.register, singledispatchmethod debe ser el decorador más externo. Aquí está la clase Negator con los métodos neg vinculados a la clase, en lugar de una instancia de la clase:

class Negator:
    @singledispatchmethod
    @classmethod
    def neg(cls, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.register
    @classmethod
    def _(cls, arg: int):
        return -arg

    @neg.register
    @classmethod
    def _(cls, arg: bool):
        return not arg



"""update_wrapper----------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Actualiza una función wrapper para que se parezca a la función wrapped. Los argumentos opcionales son tuplas para especificar qué atributos de la función original se asignan directamente a los atributos coincidentes en la función contenedora y qué atributos de la función contenedora se actualizan con los atributos correspondientes de la función original. Los valores predeterminados para estos argumentos son las constantes de nivel de módulo WRAPPER_ASSIGNMENTS (que se asigna a la función contenedora __module__, __name__, __qualname__, __annotations__ y __doc__, la cadena de caracteres de documentación) y WRAPPER_UPDATES (que actualiza el __dict__ de la función contenedora, es decir, el diccionario de instancia).

# update_wrapper() puede ser usado con otros invocables que no sean funciones. Cualquier atributo nombrado en assigned o updated que falte en el objeto que se está invoca se ignora (es decir, esta función no intentará establecerlos en la función de envoltura (wrapper)). AttributeError sigue apareciendo si la propia función de envoltura no tiene ningún atributo nombrado en updated.


"""wraps-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# Esta es una función conveniente para invocar update_wrapper() como decorador de la función cuando se define una función de envoltura (wrapper). Es equivalente a partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated).

def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print('Calling decorated function')
        return f(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')




















