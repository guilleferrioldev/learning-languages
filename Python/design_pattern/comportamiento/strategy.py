"""
Strategy es un patrón de diseño de comportamiento que te permite definir una familia de algoritmos, colocar cada uno de ellos en
una clase separada y hacer sus objetos intercambiables.

# Casos de uso 
- Utiliza el patrón Strategy cuando quieras utiliza distintas variantes de un algoritmo dentro de un objeto y poder cambiar de un
algoritmo a otro durante el tiempo de ejecución.

- Utiliza el patrón Strategy cuando tengas muchas clases similares que sólo se diferencien en la forma en que ejecutan cierto 
comportamiento.

- Utiliza el patrón para aislar la lógica de negocio de una clase, de los detalles de implementación de algoritmos que pueden no
ser tan importantes en el contexto de esa lógica.

-  Utiliza el patrón cuando tu clase tenga un enorme operador condicional que cambie entre distintas variantes del mismo algoritmo.

#  Cómo implementarlo
1. En la clase contexto, identifica un algoritmo que tienda a sufrir cambios frecuentes. También puede ser un enorme condicional 
que seleccione y ejecute una variante del mismo algoritmo durante el tiempo de ejecución.

2. Declara la interfaz estrategia común a todas las variantes del algoritmo.

3. Uno a uno, extrae todos los algoritmos y ponlos en sus propias clases. Todas deben implementar la misma interfaz estrategia.

4. En la clase contexto, añade un campo para almacenar una referencia a un objeto de estrategia. Proporciona un modificador set 
para sustituir valores de ese campo. La clase contexto debe trabajar con el objeto de estrategia únicamente a través de la interfaz 
estrategia. La clase contexto puede definir una interfaz que permita a la estrategia acceder a sus datos.

5. Los clientes de la clase contexto deben asociarla con una estrategia adecuada que coincida con la forma en la que esperan que 
la clase contexto realice su trabajo principal.

# Pros y contras
p- Puedes intercambiar algoritmos usados dentro de un objeto durante el tiempo de ejecución.

p- Puedes aislar los detalles de implementación de un algoritmo del código que lo utiliza.

p- Puedes sustituir la herencia por composición.

p- Principio de abierto/cerrado. Puedes introducir nuevas estrategias sin tener que cambiar el contexto.

c- Si sólo tienes un par de algoritmos que raramente cambian, no hay una razón real para complicar el programa en exceso con nuevas
clases e interfaces que vengan con el patrón.

c- Los clientes deben conocer las diferencias entre estrategias para poder seleccionar la adecuada.

c- Muchos lenguajes de programación modernos tienen un soporte de tipo funcional que te permite implementar distintas versiones de 
un algoritmo dentro de un grupo de funciones anónimas. Entonces puedes utilizar estas funciones exactamente como habrías utilizado
los objetos de estrategia, pero sin saturar tu código con clases e interfaces adicionales.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "b", "c", "d", "e"])
        print(",".join(result))

class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List):
        pass

class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()













