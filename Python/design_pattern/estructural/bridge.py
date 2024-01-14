"""
Bridge es un patrón de diseño estructural que te permite dividir una clase grande, o un grupo de clases estrechamente relacionadas, en dos jerarquías
separadas (abstracción e implementación) que pueden desarrollarse independientemente la una de la otra.

# Casos de uso 
- Utiliza el patrón Bridge cuando quieras dividir y organizar una clase monolítica que tenga muchas variantes de una sola funcionalidad (por ejemplo, 
si la clase puede trabajar con diversos servidores de bases de datos).

-  Utiliza el patrón cuando necesites extender una clase en varias dimensiones ortogonales (independientes).

- Utiliza el patrón Bridge cuando necesites poder cambiar implementaciones durante el tiempo de ejecución.

# Como impplementarlo 
1. Identifica las dimensiones ortogonales de tus clases. Estos conceptos independientes pueden ser: abstracción/plataforma, dominio/infraestructura,
front end/back end, o interfaz/implementación.

2. Comprueba qué operaciones necesita el cliente y defínelas en la clase base de abstracción.

3. Determina las operaciones disponibles en todas las plataformas. Declara aquellas que necesite la abstracción en la interfaz general de implementación.

4. Crea clases concretas de implementación para todas las plataformas de tu dominio, pero asegúrate de que todas sigan la interfaz de implementación.

5. Dentro de la clase de abstracción añade un campo de referencia para el tipo de implementación. La abstracción delega la mayor parte del trabajo al 
objeto de la implementación referenciado en ese campo.

6. Si tienes muchas variantes de lógica de alto nivel, crea abstracciones refinadas para cada variante extendiendo la clase base de abstracción.

7. El código cliente debe pasar un objeto de implementación al constructor de la abstracción para asociar el uno con el otro. Después, el cliente puede
ignorar la implementación y trabajar solo con el objeto de la abstracción.


# Pros y contras 
p- Puedes crear clases y aplicaciones independientes de plataforma.

p- El código cliente funciona con abstracciones de alto nivel. No está expuesto a los detalles de la plataforma.

p- Principio de abierto/cerrado. Puedes introducir nuevas abstracciones e implementaciones independientes entre sí.

p- Principio de responsabilidad única. Puedes centrarte en la lógica de alto nivel en la abstracción y en detalles de la plataforma en la implementación.

c- Puede ser que el código se complique si aplicas el patrón a una clase muy cohesionada.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstraction(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass 

class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    client_code(abstraction)

    print("\n")

    implementation = ConcreteImplementationB()
    abstraction = ExtendedAbstraction(implementation)
    client_code(abstraction)







