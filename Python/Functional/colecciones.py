from collections import Counter, namedtuple, deque, defaultdict, ChainMap 
from sys import getsizeof

"""Counter-----------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# dict subclass for counting hashable objects

counter = Counter("gallad")
counter_2 = Counter(["a", "b", "c", "d", "e"])
counter_3 = Counter([1 , 2, 3, 2, 1])
counter_4 = Counter({"a": 1, "b": 2})
counter_5 = Counter(cats = 4, dogs = 2)

# Devuelve un iterador sobre elementos que se repiten cada uno tantas veces como sea necesario. Los elementos se devuelven en el orden en que se encontraron por primera vez. Si el recuento de un elemento es menor que uno, elements() lo ignorará.
elements = counter_3.elements()

# Devuelve una lista de los n elementos más comunes y sus recuentos desde el más común al menos. Si se omite n o es Ninguno, most_common() devuelve todos los elementos del contador. Los elementos con recuentos iguales se ordenan en el orden en que se encontraron por primera vez 
most_common = counter.most_common(3)

# Es como una union de conjuntos. 
subtract = counter_2.subtract(counter)

# Computa la suma de la cuenta de todos los elementos
total = counter_5.total()

"""NamedTuple--------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# función factory para crear subclases de tuplas con campos con nombre
# La principal diferencia entre NamedTuples u las tuplas normales es que puedes indexar

point = namedtuple('Point', ['a', 'b', 'c'], defaults = [4,2,3])
point_2 = namedtuple("Punto", "x y z")

firstP = point(2,3,4)
secondP = point_2(5,6,7)

suma = firstP[1] + secondP[2]
suma_2 = firstP.b  + secondP.x

# Conviert un iteable en una namedtuple
t = [11,22,33]
make = point._make(t)

# Devuelve un diccionario de la namedtuple donde a cada llave le corresponde su valor
asdict = make._asdict()

# Reemplaza valores 
replace = make._replace(a = 1)

# Devuelve los campos 
fields = point._fields

# Devuelve los valores por defecto 
field_defaults  = point._field_defaults


"""deque-------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# contenedor similar a una lista con appends y pops rápidos en ambos extremos

deque_gui = deque("guille")

# Agregar un elemento al final 
deque_gui.append("r")

# Agregar un elemento al prinncipio 
deque_gui.appendleft("a")

# Eliminar el ultimo elemento
deque_gui.pop()

# Eliminar el primer elemento
deque_gui.popleft()

# Agregar varios elementos al final 
deque_gui.extend("rmo")

# Agregar varios elementos al principio
deque_gui.extendleft("cba")

# Rotacion hacia la izquierda
deque_gui.rotate(-1)

# Rotacion hacia la derecha
deque_gui.rotate(1)

# Cuenta cuantas veces aparece un valor 
count = deque_gui.count("l")

# Invertir el deque
reverse  = deque(reversed(deque_gui))

# Insertar en una posicion un elemento
deque_gui.insert(3, "d")

# Limpiar por completo 
deque_gui.clear()


"""defaultdict-------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# subclase de dict que llama a una función de factory para suministrar valores faltantes
# Retorna un nuevo objeto similar a un diccionario. defaultdict es una subclase de la clase incorporada dict. Anula un método y agrega una variable de instancia de escritura. La funcionalidad restante es la misma que para la clase dict 

s = [('y', 1), ('b', 2), ('y', 3), ('b', 4), ('r', 1)]
d1 = defaultdict(list)

for k, v in s:
    d1[k].append(v)

# print(d1.items())

s = 'mississippi'
d2 = defaultdict(int)

for k in s:
    d2[k] += 1

# print(d2)


"""ChainMap----------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
# clase similar a dict para crear una vista única de múltiples mapeados
# Un ChainMap agrupa varios diccionarios u otros mappings para crear una vista única y actualizable. Si no se especifican maps, se proporciona un solo diccionario vacío para que una nueva cadena siempre tenga al menos un mapeo.

# Es más rápido que hacer un update entre diccionarios. Y es lo mismo
# 

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"d": 4, "e": 5}
d3 = {"f": 6, "g": 7}

chainmap = ChainMap(d1, d2)
# Retorna un nuevo ChainMap conteniendo un nuevo mapa seguido de todos los mapas de la instancia actual.
new_child = chainmap.new_child(d3)

# Devuelve una list de todos los elementos
maps = chainmap.maps

# Propiedad que retorna un nuevo ChainMap conteniendo todos los mapas de la instancia actual excepto el primero.
parents = chainmap.parents


