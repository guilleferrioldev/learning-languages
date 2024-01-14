"""
Abstract Factory es un patrón de diseño creacional que nos permite producir familias de objetos relacionados sin especificar sus clases concretas.

# Casos de uso 
- Utiliza el patrón Abstract Factory cuando tu código deba funcionar con varias familias de productos relacionados, pero no desees que dependa de las clases
concretas de esos productos, ya que puede ser que no los conozcas de antemano o sencillamente quieras permitir una futura extensibilidad.

- Considera la implementación del patrón Abstract Factory cuando tengas una clase con un grupo de métodos de fábrica que nublen su responsabilidad principal.

# Como implementarlo
1. Mapea una matriz de distintos tipos de productos frente a variantes de dichos productos.

2. Declara interfaces abstractas de producto para todos los tipos de productos. Después haz que todas las clases concretas de productos implementen esas
interfaces.

3. Declara la interfaz de la fábrica abstracta con un grupo de métodos de creación para todos los productos abstractos.

4. Implementa un grupo de clases concretas de fábrica, una por cada variante de producto.

5. Crea un código de inicialización de la fábrica en algún punto de la aplicación. Deberá instanciar una de las clases concretas de la fábrica, dependiendo 
de la configuración de la aplicación o del entorno actual. Pasa este objeto de fábrica a todas las clases que construyen productos.

6. Explora el código y encuentra todas las llamadas directas a constructores de producto. Sustitúyelas por llamadas al método de creación adecuado dentro 
del objeto de fábrica.

# Pros y contras
p- Puedes tener la certeza de que los productos que obtienes de una fábrica son compatibles entre sí.

p-  Evitas un acoplamiento fuerte entre productos concretos y el código cliente.

p- Principio de responsabilidad única. Puedes mover el código de creación de productos a un solo lugar, haciendo que el código sea más fácil de mantener.

p- Principio de abierto/cerrado. Puedes introducir nuevas variantes de productos sin descomponer el código cliente existente.

c- Puede ser que el código se complique más de lo que debería, ya que se introducen muchas nuevas interfaces y clases junto al patrón.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


"""Abstraccion de las fabricas"""
class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abstractmethod
    def create_sofa(self) -> AbstractSofa:
        pass

# Fabrica Moderna (concreta)
class ModernFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return ModernChair()

    def create_sofa(self) -> AbstractSofa:
        return ModernSofa()

# Vieja fabrica (concreta)
class OldFactory(AbstractFactory):
    def create_chair(self) -> AbstractChair:
        return OldChair()

    def create_sofa(self) -> AbstractSofa:
        return OldSofa()

"""Abstraccion de las silla"""
class AbstractChair(ABC):
    @abstractmethod
    def create_a_chair(self) -> str:
        pass

# Silla moderna (concreta)
class ModernChair(AbstractChair):
    def create_a_chair(self) -> str:
        return "Modern Chair"

# Silla vieja (concreta)
class OldChair(AbstractChair):
    def create_a_chair(self) -> str:
        return "Old Chair"


"""Abstracciones de los sofas"""
class AbstractSofa(ABC):
    @abstractmethod
    def create_a_sofa(self) -> None:
        pass

    @abstractmethod
    def another_create_a_sofa(self, collaborator: AbstractChair) -> None:
        pass

# Sofa moderno (concreto)
class ModernSofa(AbstractSofa):
    def create_a_sofa(self) -> str:
        return "The result of the product Modern Sofa."

    def another_create_a_sofa(self, collaborator: AbstractChair) -> str:
        result = collaborator.create_a_chair()
        return f"The result of the Modern Sofa collaborating with the ({result})"

# Sofa viejo (concreto)
class OldSofa(AbstractSofa):
    def create_a_sofa(self) -> str:
        return "The result of the product Old Chair."

    def another_create_a_sofa(self, collaborator: AbstractChair):
        result = collaborator.create_a_chair()
        return f"The result of the Old Sofa collaborating with the ({result})"


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_chair()
    product_b = factory.create_sofa()

    print(f"{product_b.create_a_sofa()}")
    print(f"{product_b.another_create_a_sofa(product_a)}", end="")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(ModernFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(OldFactory())
