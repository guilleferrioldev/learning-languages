"""
Template Method es un patrón de diseño de comportamiento que define el esqueleto de un algoritmo en la superclase pero permite 
que las subclases sobrescriban pasos del algoritmo sin cambiar su estructura.

# Casos de uso 
-  Utiliza el patrón Template Method cuando quieras permitir a tus clientes que extiendan únicamente pasos particulares de un 
algoritmo, pero no todo el algoritmo o su estructura.

-  Utiliza el patrón cuando tengas muchas clases que contengan algoritmos casi idénticos, pero con algunas diferencias mínimas. 
Como resultado, puede que tengas que modificar todas las clases cuando el algoritmo cambie.

# Cómo implementarlo
1. Analiza el algoritmo objetivo para ver si puedes dividirlo en pasos. Considera qué pasos son comunes a todas las subclases y 
cuáles siempre serán únicos.

2. Crea la clase base abstracta y declara el método plantilla y un grupo de métodos abstractos que representen los pasos del 
algoritmo. Perfila la estructura del algoritmo en el método plantilla ejecutando los pasos correspondientes. Considera declarar 
el método plantilla como final para evitar que las subclases lo sobrescriban.

3. No hay problema en que todos los pasos acaben siendo abstractos. Sin embargo, a algunos pasos les vendría bien tener una 
implementación por defecto. Las subclases no tienen que implementar esos métodos.

4. Piensa en añadir ganchos entre los pasos cruciales del algoritmo.

5. Para cada variación del algoritmo, crea una nueva subclase concreta. Ésta debe implementar todos los pasos abstractos, pero
también puede sobrescribir algunos de los opcionales.

# Pros y contras
p- Puedes permitir a los clientes que sobrescriban tan solo ciertas partes de un algoritmo grande, para que les afecten menos los
cambios que tienen lugar en otras partes del algoritmo.

p- Puedes colocar el código duplicado dentro de una superclase.

c-Algunos clientes pueden verse limitados por el esqueleto proporcionado de un algoritmo.

c- Puede que violes el principio de sustitución de Liskov suprimiendo una implementación por defecto de un paso a través de una 
subclase.

c- Los métodos plantilla tienden a ser más difíciles de mantener cuantos más pasos tengan.
"""

from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def template_method(self) -> None:
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


def client_code(abstract_class: AbstractClass) -> None:
    abstract_class.template_method()


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
