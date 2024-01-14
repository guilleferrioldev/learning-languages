"""
Memento es un patrón de diseño de comportamiento que te permite guardar y restaurar el estado previo de un objeto sin revelar 
los detalles de su implementación.

# Casos de uso  
-  Utiliza el patrón Memento cuando quieras producir instantáneas del estado del objeto para poder restaurar un estado previo del
objeto.

-  Utiliza el patrón cuando el acceso directo a los campos, consultores o modificadores del objeto viole su encapsulación.

# Cómo implementarlo
1. Determina qué clase jugará el papel de la originadora. Es importante saber si el programa utiliza un objeto central de este tipo
o varios más pequeños.

2. Crea la clase memento. Uno a uno, declara un grupo de campos que reflejen los campos declarados dentro de la clase originadora.

3. Haz la clase memento inmutable. Una clase memento debe aceptar los datos sólo una vez, a través del constructor. La clase no debe
tener modificadores.

4. Si tu lenguaje de programación soporta clases anidadas, anida la clase memento dentro de la originadora. Si no es así, extrae una
interfaz en blanco de la clase memento y haz que el resto de objetos la utilicen para remitirse a ella. Puedes añadir operaciones de
metadatos a la interfaz, pero nada que exponga el estado de la originadora.

5. Añade un método para producir mementos a la clase originadora. La originadora debe pasar su estado a la clase memento a través de
uno o varios argumentos del constructor del memento.

6. Añade un método para restaurar el estado del originador a su clase. Debe aceptar un objeto memento como argumento. Si extrajiste 
una interfaz en el paso previo, haz que sea el tipo del parámetro. En este caso, debes especificar el tipo del objeto entrante al 
de la clase memento, ya que la originadora necesita pleno acceso a ese objeto.

7. La cuidadora, independientemente de que represente un objeto de comando, un historial, o algo totalmente diferente, debe saber
cuándo solicitar nuevos mementos de la originadora, cómo almacenarlos y cuándo restaurar la originadora con un memento particular.

8. El vínculo entre cuidadoras y originadoras puede moverse dentro de la clase memento. En este caso, cada memento debe conectarse
a la originadora que lo creó. El método de restauración también se moverá a la clase memento. No obstante, todo esto sólo tendrá
sentido si la clase memento está anidada dentro de la originadora o la clase originadora proporciona suficientes modificadores 
para sobrescribir su estado.

# Pros y contras
p-  Puedes producir instantáneas del estado del objeto sin violar su encapsulación.

p- Puedes simplificar el código de la originadora permitiendo que la cuidadora mantenga el historial del estado de la originadora.

c-  La aplicación puede consumir mucha memoria RAM si los clientes crean mementos muy a menudo.

c- Las cuidadoras deben rastrear el ciclo de vida de la originadora para poder destruir mementos obsoletos.

c- La mayoría de los lenguajes de programación dinámicos, como PHP, Python y JavaScript, no pueden garantizar que el estado dentro 
del memento se mantenga intacto.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters

class Originator:
    _state = None

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()

