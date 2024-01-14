"""
Iterator es un patrón de diseño de comportamiento que te permite recorrer elementos de una colección sin exponer su representación
subyacente (lista, pila, árbol, etc.).

# Casos de uso 
- Utiliza el patrón Iterator cuando tu colección tenga una estructura de datos compleja a nivel interno, pero quieras ocultar su
complejidad a los clientes (ya sea por conveniencia o por razones de seguridad).

- Utiliza el patrón para reducir la duplicación en el código de recorrido a lo largo de tu aplicación.

-  Utiliza el patrón Iterator cuando quieras que tu código pueda recorrer distintas estructuras de datos, o cuando los tipos de 
estas estructuras no se conozcan de antemano.

# Cómo implementarlo
1. Declara la interfaz iteradora. Como mínimo, debe tener un método para extraer el siguiente elemento de una colección. Por 
conveniencia, puedes añadir un par de métodos distintos, como para extraer el elemento previo, localizar la posición actual o 
comprobar el final de la iteración.

2. Declara la interfaz de colección y describe un método para buscar iteradores. El tipo de retorno debe ser igual al de la 
interfaz iteradora. Puedes declarar métodos similares si planeas tener varios grupos distintos de iteradores.

3. Implementa clases iteradoras concretas para las colecciones que quieras que sean recorridas por iteradores. Un objeto iterador 
debe estar vinculado a una única instancia de la colección. Normalmente, este vínculo se establece a través del constructor del
iterador.

4. Implementa la interfaz de colección en tus clases de colección. La idea principal es proporcionar al cliente un atajo para 
crear iteradores personalizados para una clase de colección particular. El objeto de colección debe pasarse a sí mismo al 
constructor del iterador para establecer un vínculo entre ellos.

5. Repasa el código cliente para sustituir todo el código de recorrido de la colección por el uso de iteradores. El cliente busca 
un nuevo objeto iterador cada vez que necesita recorrer los elementos de la colección.

# Pros y contras
p- Principio de responsabilidad única. Puedes limpiar el código cliente y las colecciones extrayendo algoritmos de recorrido 
voluminosos y colocándolos en clases independientes.

p- Principio de abierto/cerrado. Puedes implementar nuevos tipos de colecciones e iteradores y pasarlos al código existente sin 
descomponer nada.

p- Puedes recorrer la misma colección en paralelo porque cada objeto iterador contiene su propio estado de iteración.

p- Por la misma razón, puedes retrasar una iteración y continuar cuando sea necesario.

c- Aplicar el patrón puede resultar excesivo si tu aplicación funciona únicamente con colecciones sencillas.

c- Utilizar un iterador puede ser menos eficiente que recorrer directamente los elementos de algunas colecciones especializadas.
"""


from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


class AlphabeticalOrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")