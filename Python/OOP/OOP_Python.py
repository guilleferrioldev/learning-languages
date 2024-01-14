"""Herencia"""
class Persona:
    def __init__(self, nombre: str, edad: int, nacionalidad: str):
        self.nombre: str = nombre 
        self.edad: int = edad 
        self.nacionalidad: str = nacionalidad 
    
    def mostrar_datos(self) -> str:
        return f"Mi nombre es {self.nombre}\nMi edad es {self.edad}\nMi nacionalidad es {self.nacionalidad}"

class Artista:
    def __init__(self, habilidad: str):
        self.habilidad: str = habilidad

    def mostrar_habilidad(self) -> str:
        return f"Mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre: str, edad: int, nacionalidad: str, habilidad: str, salario: float, empresa: str):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario: float = salario
        self.empresa: str = empresa 

    def presentarse(self) -> str:
        return f"{super().mostrar_datos()}\n{super().mostrar_habilidad()}\nTrabajo en {self.empresa}\nMi salario es de {self.salario}"

# Crear el objeto
manuel: EmpleadoArtista = EmpleadoArtista("Manuel", 15, "Cuba","cantar",4000, "ONBC")

# Preguntar si hereda de alguna  clase en específico
herencia: bool = issubclass(EmpleadoArtista, Persona)
# print(herencia) # -> True 

# Preguntar si un objeto es una instancia de una clase
instancia: bool = isinstance(manuel, Artista)
#print(instancia) # -> True 




"""Polimorfismo"""
# Duck Typing
# Tipo real y declarado
# Enlaces dinámicos y estáticos


class Pato:
    def parpar(self) -> str: 
        return f"Cuac!"

    def plumas(self) -> str: 
        return f"El pato tiene plumas blancas y grises."
 
class Persona:
    def parpar(self) -> str:
        return f"La persona imita el sonido de un pato."

    def plumas(self) -> str: 
        return f"La persona toma una pluma del suelo y la muestra."
 
def en_el_bosque(pato) -> None:
    print(pato.parpar())
    print(pato.plumas())
 
def juego() -> None:
    donald = Pato()
    juan = Persona()
    en_el_bosque(donald)
    en_el_bosque(juan)



"""Encapsulamiento"""
class MiClase:
    def __init__(self):
        self.publico: str = "público"
        self._privado: str = "privado"
        self.__encapsulado: str = "encapsulado"
    
    # metodo privado
    def _saludar(self) -> str:
        return "hola, como estas"
    
    # metodo encapsulado
    def __hablar(self) -> str:
        return "hola, como estas"


# Los getters y setters son metodos para acceder y modificar los atributos privados y encapsulado
class Person:
    def __init__(self, nombre: str, edad: int):
        self.__nombre: str = nombre 
        self._edad: int = edad
    
    # getter
    @property 
    def _get_name(self) -> str:
        return self.__nombre 
    
    # setter
    @_get_name.setter
    def _set_name(self, new_name: str) -> None:
        self.__nombre: str = new_name

    # deleter
    @_get_name.deleter
    def _del_name(self) -> None:
        del self.__nombre

guille: Person = Person("Guille", 22)
#print(guille._get_name) # -> Guille

guille._set_name = "Dalto"
#print(guille._get_name) # -> Dalto

del guille._del_name
#print(guille._get_name) # -> Error xq el nombre ya se eliminó




"""Decoradores"""
# Toma una función como entrada, le agrega funcionalidades extras y devuelve como salida la funcion modificada 
# Son usados para el manejo de excepciones, validación de entrada, medición del tiempo de ejecución, etc 

from time import time

def time_counter(funcion) -> None:
    def funcion_modificada() -> None:
        start: str = time()
        print(funcion())
        print(f"Ha tardado {time() - start}")
    return funcion_modificada

@time_counter
def count_to_5() -> list:
    return [i for i in range(6)]

@time_counter
def count_to_6() -> list:
    result: list = []
    for i in range(7):
        result.append(i)
    return result



"""Abtracción"""
# Es manejar la complejidad, ocultando todos los detalles necesarios al programador o al usuario y dándole sólo las funcionalidades relevante 

class Auto: 
    def __init__(self):
        self._estado: str = "apagado"

    def encender(self) -> str:
        self._estado = "encendido"
        return "El auto está encendido"

    def conducir(self) -> str:
        if self._estado == "apagado":
            self.encender()
        return "Conduciendo el auto"

auto = Auto()
# print(auto.conducir()) # -> "Conduciendo el auto"


"""Clases abstractas"""
# Es una clase que no podemos instanciar pero es como una especie de plantilla para que se puedan crear clases a partir de esa plantilla
# Estas clases aumentan la seguridad
# Un método abstracto es un método que está declarado en la clase abstracta, sólo que no tiene ninguna implementación 

from abc import ABC, abstractclassmethod

class Persons(ABC):
    @abstractclassmethod
    def __init__(self, nombre: str, edad: int, sexo: str, actividad: str):
        self.nombre: str = nombre
        self.edad: int = edad
        self.sexo: str = sexo 
        self.actividad: str = actividad

    @abstractclassmethod 
    def hacer_actividad(self) -> str:
        pass

    def presentarse(self) -> str:
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años"


class Student(Persons):
    def __init__(self, nombre: str, edad: int, sexo: str, actividad: str):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self) -> str:
        return f"Estoy estudiando {self.actividad}"

class Worker(Persons):
    def __init__(self, nombre: str, edad: int, sexo: str, actividad: str):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self) -> str:
        return f"Actualmente estoy trabajando en el rubro de {self.actividad}"



guille: Student = Student("Guille", 23, "M", "programación")
dalto: Worker = Worker("Dalto", 25, "M", "programación")


# print(guille.hacer_actividad()) # -> "Estoy estudiando programación"
# print(dalto.hacer_actividad()) # -> "Actualmente estoy trabajando en el rubro de programación"


"""Métodos Dunder"""
class Personita:
    # método constuctor
    def __init__(self, nombre: str, edad: str):
        self.nombre: str = nombre
        self.edad: str = edad

    # Método que devuelve la representación del objeto en una cadena de textos
    # Sirve para hacer el print directamente
    def __str__(self) -> str:
        return f"Personita(nombre={self.nombre},edad={self.edad})"

    # Lo mismo que la función anterior
    def __repr__(self) -> str:
        return f"Personita('{self.nombre}',{self.edad})"
    
    # Sumar valores con otra clase  
    def __add__(self, otro) -> None:
        nuevo_valor = self.edad + otro.edad
        return Personita(self.nombre + otro.nombre, nuevo_valor)


guille: Personita = Personita("Guille", 23)
## Métodos de representación
# print(guille)
# print(repr(guille))

## Metodo add
pedro: Personita = Personita("Pedro", 30)
maria: Personita = Personita("Maria", 52)
result: Personita = guille + pedro + maria
# print(result.edad) # -> 105


