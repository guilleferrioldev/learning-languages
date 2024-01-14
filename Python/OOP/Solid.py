# Es un conjunto de principios que se utilizan para hacer que los diseños sean más comprensible, flexibles, escalables y resistentes a los cambios.

"""SRP : Single Responsability Principle"""
# Cada clase tiene que tener una y sólo una razón para cambiar. Tiene que tener una única tarea


class TankeDeCombustible():
    def __init__(self):
        self._combustible: float = 100
    
    @property
    def obtener_combustible(self) -> float:
        return self._combustible 
    
    @obtener_combustible.setter
    def agregar_combustible(self, cantidad: float) -> None:
        self._combustible += cantidad
    
    @obtener_combustible.setter
    def usar_combustible(self, cantidad: float) -> None:
        self._combustible -= cantidad


class Auto():
    def __init__(self, tanque: TankeDeCombustible):
        self._posicion: float = 0
        self.__tanque: TankeDeCombustible = tanque

    @property 
    def obtener_posicion(self) -> float:
        return self._posicion
        
    @property 
    def obtener_tanque(self) -> TankeDeCombustible:
        return self.__tanque

    @obtener_posicion.setter
    def aumentar_posicion(self, distancia: float) -> float:
        self._posicion += distancia
    
    def mover(self, distancia: float) -> str: #max == 200
        if self.obtener_tanque.obtener_combustible >= distancia / 2:
            self.aumentar_posicion = distancia 
            self.obtener_tanque.usar_combustible = distancia / 2
            return "Has movido el auto exitosamente" 
        else:
            return "No hay suficiente combustible"

### TEST
#tanque = TankeDeCombustible()
#auto = Auto(tanque)
#print(auto.mover(10))
#print(auto.obtener_posicion)


"""OCP Open/Closed Principle"""
# Las clases tienen que estar abiertas para la extensión  pero cerradas para la modificación 

class Usuario():
    def __init__(self):
        self.__nombre = "Guillermo Ferriol"
        self.__email = "guille@gmail.com"

    @property 
    def get_name(self) -> str:
        return self.__nombre

    @property 
    def get_email(self) -> str:
        return self.__email


class Notificador():
    def __init__(self, usuario: Usuario):
        self.usuario: str = usuario.get_name
        self.email: str = usuario.get_email

    def notificar(self) -> None:
        raise NotImplementedError 


class NotificadorEmail(Notificador):
    def __init__(self, usuario: Usuario):
        super().__init__(usuario)

    def notificar(self) -> str:
        return f"Enviado mensaje a {self.email}"


### TEST
#usuario = Usuario()
#notificar = NotificadorEmail(usuario)
#print(notificar.notificar())


"""LSP Liskov's substitution principle"""
# Las clases derivadas tienen que ser sustituibles por sus cases bases
# Si la clase B es una subclase de A, la clase A debería poder utilizarse en todos los lugares en donde B pueda utilizarse 

class Ave():
    def volar(self) -> str:
        pass

    def nadar(self) -> str:
        pass

class AveVoladora(Ave):
    def volar(self) -> str :
        return "Estoy volando"
       
class AveNadadora(Ave):
    def nadar(self) -> str :
        return "Estoy nadando"

class Pinguino(AveNadadora):
    pass


### TEST
#pinguino = Pinguino()
#print(pinguino.nadar())



"""ISP Interface Segregation Principle"""
# Ningún cliente tiene que ser forzado a depender de interfaces que no utilice. Eliminar las dependencias que no se van a utilizar

from abc import ABC, abstractmethod 

class Trabajador(ABC):
    @abstractmethod 
    def trabajar(self):
        pass 

class Comedor(ABC):
    @abstractmethod 
    def comer(self):
        pass 

class Durmiente(ABC):
    @abstractmethod 
    def dormir(self):
        pass 

class Humano(Trabajador, Durmiente, Comedor):
    def comer(self) -> str:
        return "El humano está comiendo"

    def trabajar(self) -> str:
        return "El humano está trabajando"
    
    def dormir(self) -> str:
        return "El humano está durmiento"


class Robot(Trabajador):
    def trabajar(self) -> str:
        return "El humano está trabajando"

### TEST
#humano = Humano()
#robot = Robot()
#print(humano.comer())
#print(robot.trabajar())


"""DIP Dependency Inversion Principle"""
# Los módulos de alto nivel no tienen que depender de los de bajo nivel, los 2 deben depender de las abstacciones. 
# Las abstracciones no deben depender de los detalles, sino que al revés 

class VerificadorOrtografico(ABC):
    @abstractmethod 
    def verificar_palabra(self, palabra):
        pass 

class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra) -> str:
        # Logica para verificar palabra
        pass 

class VerificadorOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra) -> str:
        # Logica para verificar palabra
        pass 

class CorrectorOrtograficor:
    def __init__(self, verificador):
        self.verificador = verificador 

    def corregir_text(self, palabra):
        # usamos el verificador para corregir la palabra
        pass 

    
### Examples
#corrector = CorrectorOrtograficor(Diccionario())
#corrector = CorrectorOrtograficor(VerificadorOnline())
