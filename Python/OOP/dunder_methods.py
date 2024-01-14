class Person():
    def __init__(self, name, age, city):
        self.name = name 
        self.age = age 
        self.city = city
    
    # Imprimir el objeto de una manera más formal
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, city='{self.city}')"
    
    # Imprimir el objeto de una manera más oficial
    def __str__(self): 
        return f"{self.name}({self.age}) from {self.city}"
    
    # Less than (lt) < 
    def __lt__(self, other):
        return self.age < other.age
    
    # Less and equal than (le) <=
    def __le__(self, other):
        return self.age <= other.age

    # Greater than (gt) > 
    def __gt__(self, other):
        return self.age > other.age
    
    # Greater and equal than (ge) >= 
    def __ge__(self, other):
        return self.age >= other.age

    # Equal than (iq) ==. 
    def __eq__(self, other):
        return self.name == other.name
    
    # Not equal than (ne) !=. 
    def __ne__(self, other):
        return self.name != other.name
    
    # Crear un hash de seguridad para la clase
    def __hash__(self):
        return hash((self.name, self.age, self.city))
    
    # Dice si un objeto es True o False. Sirve para ccuando queremos usar condicionales
    def __bool__(self):
        if self.name and self.age and self.city:
            return True
        else:
            return False
    
    # Suma esta clase con otra
    def __add__(self, other):
        return Person(f"{self.name}/{other.name}", self.age + other.age, f"{self.city}/{other.city}")
    
    # Resta esta clase con otra
    def __sub__(self, other):
        return Person(f"{self.name}/{other.name}", self.age - other.age, f"{self.city}/{other.city}")
    
    # Multiplicar esta clase con otra
    def __mul__(self, other):
        return Person(f"{self.name}/{other.name}", self.age * other.age, f"{self.city}/{other.city}")
    
    # Dividir esta clase con otra
    def __truediv__(self, other):
        return Person(f"{self.name}/{other.name}", self.age / other.age, f"{self.city}/{other.city}")
    
    # Division esta clase con otra
    def __floordiv__(self, other):
        return Person(f"{self.name}/{other.name}", self.age // other.age, f"{self.city}/{other.city}")
    
    # Resto de la division entera 
    def __mod__(self, other):
        return Person(f"{self.name}/{other.name}", self.age % other.age, f"{self.city}/{other.city}")




# Para emular tipos de contenedores
class Containers:
    def __init__(self, content):
        self.content = content
        self.type = type(content)
    
    # Medir la longitud del iterable
    def __len__(self) -> int:
        return len(self.content)
        
    # Iterar sobre el contenido
    def __iter__(self):
        if isinstance(self.content, dict):
            return iter(self.content.items())
        else:
            return iter(self.content)
   
    # Indexar 
    def __getitem__(self, key):
        return self.content[key]
        
    # Agregar elemento
    def __setitem__(self, key, value):
        if isinstance(self.content, set):
            raise TypeError
        else: 
            self.content[key] = value
    
    # Para utilizar en condicionales cuando preguntas si existe (if n in x)
    def __contains__(self, value):
        if value in self.content:
            return True 
        else:
            return False

    # Eliminar elemento
    def __delitem__(self, key):
        if isinstance(self.content, set):
            raise TypeError
        else: 
            del self.content[key]
    
    # Revertir elementos
    def __reversed__(self):
        if isinstance(self.content, dict):
            raise TypeError 
        else:
            return self.content[::-1]

    def __str__(self):
        return f"{self.content}, {self.type}"

































