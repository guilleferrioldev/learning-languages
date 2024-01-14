# Init vs New

# __new__() Este es el método encargado de crear al objeto, pero no de asignarle valores iniciales. Debe retornar como resultado el objeto que ha creado. Recibe como parámetro la clase a la que se supone que debería pertenecer el objeto creado. Cabe esperar que el objeto que se crea y se retorna desde __new__() pertenecerá a esa clase también, pero realmente no es obligatorio (lo que puede llevar a cosas bien raras)

# __init__() este es el método encargado de asignar valores iniciales al objeto creado desde __new__(). Como primer parámetro recibe el objeto en cuestión que debe ser inicializado (típicamente el parámetro a través del cual lo recibe se llama self).


class Connection:
    __instance = None 

    def __new__(cls, *args, **kwargs) -> None:
        if cls.__instance is None:
            print("...connecting")
            cls.__instance  = super().__new__(cls)
            return cls.__instance
        else:
            print("WARNING: There\'s already an instance of connection!")

    def __init__(self) -> None:
        print("Connected  to the internet")


from abc import ABC, abstractmethod , abstractclassmethod

class VehicleAbstract(ABC):
    @abstractclassmethod
    def __new__(cls, wheels: int):
        if wheels == 2:
            return Motobike()
        elif wheels == 4:
            return Car()
        else:
            return super().__new__(cls)

    @abstractmethod
    def __init__(self, wheels: int):
        self.wheels = wheels
        print(f"Initializing vehicle with {self.wheels} wheels")

class Vehicle(VehicleAbstract):
    def __new__(cls, wheels: int) -> None:
        super().__new__(wheels)
       
    def __init__(self, wheels: int) -> None:
        super().__new__(wheels)

class Motobike:
    def __init__(self) -> None:
        print("Initializing motobike")

class Car:
    def __init__(self) -> None:
        print("Initializing car")



