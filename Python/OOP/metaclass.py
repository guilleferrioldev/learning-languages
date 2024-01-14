class MetaClass(type):
    #Este es responsable de la creación real del objeto de clase de la misma manera que lo hace para las clases ordinarias.
    def __new__(mcs, name, bases, namespace):  
        print(mcs, "new_called")
        return super().__new__(mcs, name, bases, namespace)  
    
    # Esto crea un objeto de espacio de nombres vacío. De forma predeterminada, devuelve una instancia de dict vacía, pero se puede anular para devolver cualquier otra instancia de subclase de dict. Tenga en cuenta que no acepta el espacio de nombres como argumento porque, antes de llamarlo, el espacio de nombres aún no existe.
    @classmethod  
    def __prepare__(mcs, name, bases, **kwargs):  
        return super().__prepare__(name, bases, **kwargs)  
    
    # Esto no se ve popularmente en las implementaciones de metaclases, pero tiene el mismo significado que en las clases ordinarias. Puede realizar una inicialización de objetos de clase adicional una vez que se crea con __new__(). Cuando se llama a __init__(), la clase ya se ha construido y, por lo tanto, el método __init__() puede hacer menos que el método __new__(). 
    def __init__(cls, name, bases, namespace, **kwargs):  
        super().__init__(name, bases, namespace)  
    
    # Esto se llama cuando se llama una instancia de una metaclase. La instancia de una metaclase es un objeto de clase; se invoca cuando se crean nuevas instancias de una clase. Esto se puede utilizar para anular la forma predeterminada de cómo se crean e inicializan las instancias de clase.
    def __call__(cls, *args, **kwargs):  
        return super().__call__(*args, **kwargs)  

## Class es una palabra clave que en python son usadas para construir tipos.
## Metaclass es una clase que hereda de type
#print(type(MetaClass)) # -> <class 'type'>  type(name, bases, namespace) 

## -> name: Este es el nombre de la clase que se almacenará en el atributo __name__   
#print(MetaClass.__name__) # -> MetaClass 

## Esta es la lista de clases principales que se convertirán en el atributo __bases__ y se usarán para construir el MRO de una clase recién creada.
#print(MetaClass.__bases__) # -> (<class 'type>')

## Este es un espacio de nombres (mapeo) con definiciones para el cuerpo de la clase que se convertirá en el atributo __dict__
#print(MetaClass.__dict__)




class CustomDict(dict):
    def __setitem__(self, key, value):
        print(f"setting {key} to {value}")
        super().__setitem__(key, value)


class PrintAssignmentMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return CustomDict()
    
    def __new__(cls, name, bases, namespace):
        return super().__new__(cls, name, bases, namespace)


class PrintAssignmentClass(metaclass=PrintAssignmentMeta):
    # these print
    a = 3
    b = 4

# this does not print because the class-namespace no longer involves your custom setitem
PrintAssignmentClass.c = 5

# but all three are in the namespace of the class
print(PrintAssignmentClass.a, PrintAssignmentClass.b, PrintAssignmentClass.c)
print(PrintAssignmentClass.__dict__)

