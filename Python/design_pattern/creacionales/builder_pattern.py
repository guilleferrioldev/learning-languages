"""
Builder es un patrón de diseño creacional que nos permite construir objetos complejos paso a paso. El patrón nos permite producir distintos tipos 
y representaciones de un objeto empleando el mismo código de construcción.

# Casos de uso
- Utiliza el patrón Builder para evitar un “constructor telescópico” (con muchos parametros)

- Utiliza el patrón Builder cuando quieras que el código sea capaz de crear distintas representaciones de ciertos productos.

-  Utiliza el patrón Builder para construir árboles con el patrón Composite u otros objetos complejos.


# Como implementarlo
1. Asegúrate de poder definir claramente los pasos comunes de construcción para todas las representaciones disponibles del producto. De lo contrario,
no podrás proceder a implementar el patrón.

2. Declara estos pasos en la interfaz constructora base.

3. Crea una clase constructora concreta para cada una de las representaciones de producto e implementa sus pasos de construcción.

4. Piensa en crear una clase directora. Puede encapsular varias formas de construir un producto utilizando el mismo objeto constructor.

5. El código cliente crea tanto el objeto constructor como el director. Antes de que empiece la construcción, el cliente debe pasar un objeto constructor
al director. Normalmente, el cliente hace esto sólo una vez, mediante los parámetros del constructor del director. El director utiliza el objeto
constructor para el resto de la construcción. Existe una manera alternativa, en la que el objeto constructor se pasa directamente al método de 
construcción del director.

6. El resultado de la construcción tan solo se puede obtener directamente del director si todos los productos siguen la misma interfaz. De lo contrario,
el cliente deberá extraer el resultado del constructor.


# Pros y contras
p- Puedes construir objetos paso a paso, aplazar pasos de la construcción o ejecutar pasos de forma recursiva.

p- Puedes reutilizar el mismo código de construcción al construir varias representaciones de productos.

p- Principio de responsabilidad única. Puedes aislar un código de construcción complejo de la lógica de negocio del producto.

c-  La complejidad general del código aumenta, ya que el patrón exige la creación de varias clases nuevas.

"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Car(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def car_body(self) -> None:
        pass

    @abstractmethod
    def autopilot(self) -> None:
        pass

    @abstractmethod
    def battery(self) -> None:
        pass


class ConcreteCar(Car):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Tesla()

    @property
    def product(self) -> Tesla:
        product = self._product
        self.reset()
        return product

    def car_body(self) -> None:
        self._product.add("Car body")

    def autopilot(self) -> None:
        self._product.add("Autopilot")

    def battery(self) -> None:
        self._product.add("Battery")


class Tesla():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Car:
        return self._builder

    @builder.setter
    def builder(self, builder: Car) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.car_body()

    def build_full_featured_product(self) -> None:
        self.builder.car_body()
        self.builder.autopilot()
        self.builder.battery()


if __name__ == "__main__":
    director = Director()
    builder = ConcreteCar()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.car_body()
    builder.autopilot()
    builder.product.list_parts()




