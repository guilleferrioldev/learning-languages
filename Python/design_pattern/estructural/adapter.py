"""
Adapter es un patrón de diseño estructural que permite la colaboración entre objetos con interfaces incompatibles.

# Casos de uso
- Utiliza la clase adaptadora cuando quieras usar una clase existente, pero cuya interfaz no sea compatible con el resto del código.

- Utiliza el patrón cuando quieras reutilizar varias subclases existentes que carezcan de alguna funcionalidad común que no pueda añadirse a la superclase

# Como impplementarlo 
1. Asegúrate de que tienes al menos dos clases con interfaces incompatibles

2. Declara la interfaz con el cliente y describe el modo en que las clases cliente se comunican con la clase de servicio.

3. Crea la clase adaptadora y haz que siga la interfaz con el cliente. Deja todos los métodos vacíos por ahora.

4. Añade un campo a la clase adaptadora para almacenar una referencia al objeto de servicio. La práctica común es inicializar este campo a través del 
constructor, pero en ocasiones es adecuado pasarlo al adaptador cuando se invocan sus métodos.

5. Uno por uno, implementa todos los métodos de la interfaz con el cliente en la clase adaptadora. La clase adaptadora deberá delegar la mayor parte del
trabajo real al objeto de servicio, gestionando tan solo la interfaz o la conversión de formato de los datos.

6. Las clases cliente deberán utilizar la clase adaptadora a través de la interfaz con el cliente. Esto te permitirá cambiar o extender las clases 
adaptadoras sin afectar al código cliente.


# Pros y contras
p-  Principio de responsabilidad única. Puedes separar la interfaz o el código de conversión de datos de la lógica de negocio primaria del programa.

p-  Principio de abierto/cerrado. Puedes introducir nuevos tipos de adaptadores al programa sin descomponer el código cliente existente, siempre y 
cuando trabajen con los adaptadores a través de la interfaz con el cliente.

c-  La complejidad general del código aumenta, ya que debes introducir un grupo de nuevas interfaces y clases. En ocasiones resulta más sencillo 
cambiar la clase de servicio de modo que coincida con el resto de tu código.

"""


class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
