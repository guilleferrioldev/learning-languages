"""
Visitor es un patrón de diseño de comportamiento que te permite separar algoritmos de los objetos sobre los que operan.

# Casos de uso 
- Utiliza el patrón Visitor cuando necesites realizar una operación sobre todos los elementos de una compleja estructura de objetos
(por ejemplo, un árbol de objetos).

- Utiliza el patrón Visitor para limpiar la lógica de negocio de comportamientos auxiliares.

- Utiliza el patrón cuando un comportamiento solo tenga sentido en algunas clases de una jerarquía de clases, pero no en otras.

# Cómo implementarlo
1. Declara la interfaz visitante con un grupo de métodos “visitantes”, uno por cada clase de elemento concreto existente en el
 programa.

2. Declara la interfaz de elemento. Si estás trabajando con una jerarquía de clases de elemento existente, añade el método abstracto
 de “aceptación” a la clase base de la jerarquía. Este método debe aceptar un objeto visitante como argumento.

3. Implementa los métodos de aceptación en todas las clases de elemento concreto. Estos métodos simplemente deben redirigir la 
llamada a un método visitante en el objeto visitante entrante que coincida con la clase del elemento actual.

4. Las clases de elemento sólo deben funcionar con visitantes a través de la interfaz visitante. Los visitantes, sin embargo, deben 
conocer todas las clases de elemento concreto, referenciadas como tipos de parámetro de los métodos de visita.

5. Por cada comportamiento que no pueda implementarse dentro de la jerarquía de elementos, crea una nueva clase concreta visitante 
e implementa todos los métodos visitantes.

6. El cliente debe crear objetos visitantes y pasarlos dentro de elementos a través de métodos de “aceptación”.

# Pros y contras
p- Principio de abierto/cerrado. Puedes introducir un nuevo comportamiento que puede funcionar con objetos de clases diferentes sin 
cambiar esas clases.

p- Principio de responsabilidad única. Puedes tomar varias versiones del mismo comportamiento y ponerlas en la misma clase.

p- Un objeto visitante puede acumular cierta información útil mientras trabaja con varios objetos. Esto puede resultar útil cuando 
quieras atravesar una compleja estructura de objetos, como un árbol de objetos, y aplicar el visitante a cada objeto de esa 
estructura.

c- Debes actualizar todos los visitantes cada vez que una clase se añada o elimine de la jerarquía de elementos.

c- Los visitantes pueden carecer del acceso necesario a los campos y métodos privados de los elementos con los que se supone que 
deben trabajar.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):
    def accept(self, visitor: Visitor) -> None:
        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        return "A"


class ConcreteComponentB(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"


class Visitor(ABC):
    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass

class ConcreteVisitor1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor1")


class ConcreteVisitor2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + ConcreteVisitor2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + ConcreteVisitor2")


def client_code(components: List[Component], visitor: Visitor) -> None:
    for component in components:
        component.accept(visitor)

if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("The client code works with all visitors via the base Visitor interface:")
    visitor1 = ConcreteVisitor1()
    client_code(components, visitor1)

    print("It allows the same client code to work with different types of visitors:")
    visitor2 = ConcreteVisitor2()
    client_code(components, visitor2)
