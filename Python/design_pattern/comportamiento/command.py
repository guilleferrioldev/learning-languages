"""
Command es un patrón de diseño de comportamiento que convierte una solicitud en un objeto independiente que contiene toda la 
información sobre la solicitud. Esta transformación te permite parametrizar los métodos con diferentes solicitudes, retrasar
o poner en cola la ejecución de una solicitud y soportar operaciones que no se pueden realizar.

# Casos de uso 
- Utiliza el patrón Command cuando quieras parametrizar objetos con operaciones.

- Utiliza el patrón Command cuando quieras poner operaciones en cola, programar su ejecución, o ejecutarlas de forma remota.

- Utiliza el patrón Command cuando quieras implementar operaciones reversibles.

# Cómo implementarlo
1. Declara la interfaz de comando con un único método de ejecución.

2. Empieza extrayendo solicitudes y poniéndolas dentro de clases concretas de comando que implementen la interfaz de comando.
Cada clase debe contar con un grupo de campos para almacenar los argumentos de las solicitudes junto con referencias al objeto
receptor. Todos estos valores deben inicializarse a través del constructor del comando.

3. Identifica clases que actúen como emisoras. Añade los campos para almacenar comandos dentro de estas clases. Las emisoras
deberán comunicarse con sus comandos tan solo a través de la interfaz de comando. Normalmente las emisoras no crean objetos 
de comando por su cuenta, sino que los obtienen del código cliente.

4. Cambia las emisoras de forma que ejecuten el comando en lugar de enviar directamente una solicitud al receptor.

5. El cliente debe inicializar objetos en el siguiente orden:
- Crear receptores.
- Crear comandos y asociarlos con receptores si es necesario.
- Crear emisores y asociarlos con comandos específicos

# Pros y contras 
p- Principio de responsabilidad única. Puedes desacoplar las clases que invocan operaciones de las que realizan esas operaciones.

p- Principio de abierto/cerrado. Puedes introducir nuevos comandos en la aplicación sin descomponer el código cliente existente.

p- Puedes implementar deshacer/rehacer.

p- Puedes implementar la ejecución diferida de operaciones.

p- Puedes ensamblar un grupo de comandos simples para crear uno complejo.

c- El código puede complicarse, ya que estás introduciendo una nueva capa entre emisores y receptores.
"""


from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(
        receiver, "Send email", "Save report"))

    invoker.do_something_important()



