"""
Singleton es un patrón de diseño creacional que nos permite asegurarnos de que una clase tenga una única instancia, a la vez que proporciona un
punto de acceso global a dicha instancia.

# Aplicabilidad
- Utiliza el patrón Singleton cuando una clase de tu programa tan solo deba tener una instancia disponible para todos los clientes; por ejemplo,
un único objeto de base de datos compartido por distintas partes del programa.

- Utiliza el patrón Singleton cuando necesites un control más estricto de las variables globales.

# Como implementarlo
1. Añade un campo estático privado a la clase para almacenar la instancia Singleton.

2. Declara un método de creación estático público para obtener la instancia Singleton.

3. Implementa una inicialización diferida dentro del método estático. Debe crear un nuevo objeto en su primera llamada y colocarlo dentro del
campo estático. El método deberá devolver siempre esa instancia en todas las llamadas siguientes.

4. Declara el constructor de clase como privado. El método estático de la clase seguirá siendo capaz de invocar al constructor, pero no a los 
otros objetos.

5. Repasa el código cliente y sustituye todas las llamadas directas al constructor de la instancia Singleton por llamadas a su método de creación estático.

# Pros y contras
p- Puedes tener la certeza de que una clase tiene una única instancia.

p- Obtienes un punto de acceso global a dicha instancia.

p- El objeto Singleton solo se inicializa cuando se requiere por primera vez.

c- Vulnera el Principio de responsabilidad única. El patrón resuelve dos problemas al mismo tiempo.

c- El patrón Singleton puede enmascarar un mal diseño, por ejemplo, cuando los componentes del programa saben demasiado los unos sobre los otros.

c- El patrón requiere de un tratamiento especial en un entorno con múltiples hilos de ejecución, para que varios hilos no creen un objeto Singleton
varias veces.

c- Puede resultar complicado realizar la prueba unitaria del código cliente del Singleton porque muchos frameworks de prueba dependen de la herencia 
a la hora de crear objetos simulados (mock objects). Debido a que la clase Singleton es privada y en la mayoría de los lenguajes resulta imposible 
sobrescribir métodos estáticos, tendrás que pensar en una manera original de simular el Singleton. O, simplemente, no escribas las pruebas. O no utilices
el patrón Singleton.
"""

# Implementacion de Java
class User(object):
    __instance = None
    
    def __new__(cls):
        if User.__instance is None:
            print("Nueva instancia")
            User.__instance = object.__new__(cls)

        return User.__instance 


# Implementacion pythonica
def singleton(cls):
    __instances = dict()
    
    def wrapper(*args, **kwargs):
        if cls not in __instances:
            __instances[cls] = cls(*args, **kwargs)
        return __instances[cls]

    return wrapper


@singleton
class Usuario(object):
    def __init__(self, username):
        self.username = username



# Implementacion con metaclases
class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


class Businessman(metaclass=SingletonMeta):
    def __init__(self, amount: int) -> None:
        self.amount = amount
    
    def some_business_logic(self):
        pass

if __name__ == "__main__":
    User1 = User()
    User2 = User()
    
    print(User1 == User2)

    Usuario1 =  Usuario("G")
    Usuario2 =  Usuario("F")
    
    print(Usuario1.username)
    print(Usuario2.username)
    
    s1 = Businessman(500)
    s2 = Businessman(200)
    
    print(s1.amount)
    print(s2.amount)

    


