import itertools
import operator

"""Infinite loops"""# ----------------------------------------------------------------------------------

"""count"""
# Un contador infinito 
count = itertools.count(start = 5, step = -2.5)

#for i in range(10):
    #print(next(count))

"""cycle""" 
# Recorrer infinitamente un iterable 
cycle = itertools.cycle((l := [i for i in range(10)]))
cycle_2 = itertools.cycle("hola")

#for i in range(len(l)):
    #print(next(cycle_2))

"""repeat"""
# Repetir un elemento cierta cantidad de veces 
repeat = itertools.repeat([2,3], times = (t:=3))

#for i in range(t):
    #print(next(repeat))


"""Iterators"""#------------------------------------------------------------------------------------------

"""accumulate"""
# Acumula un iterable en dependencia de la funcion que le pases
accumulate = list(itertools.accumulate([1,2,3,4,5], operator.mul))
accumulate_string = list(itertools.accumulate(["a", "b", "c", "d", "e"]))

"""chain"""
# Iterar por cada elemento de cada iterable
chain = list(itertools.chain("ABC", "DEF", "GHI"))

"""chain.from_iterable"""
# Iterar sobre elemento de cada iterable
chain_from = list(itertools.chain.from_iterable([[1,2,3], [4,5,6], [7,8,9]]))
chain_from_string = list(itertools.chain.from_iterable("ABCDEFGHI"))

"""compress"""
# Devuelve un comprimido en dependencia del array de bools que se le introduzca, no importa su tamaño  
compress = list(itertools.compress('ABCDEF', [1,0,False,0,True,1]))

"""dropwhile"""
# Eliminar elementos del iterable en dependencia de la funcion que se le pase hasta que este se vuelva falso 
dropwhile = list(itertools.dropwhile(lambda x: x<5, [1,4,3,6,6,1]))

"""takewhile"""
# Devuelve elementos del iterable en dependencia de la funcion que se le pase hasta que este se vuelva falso 
takewhile = list(itertools.takewhile(lambda x: x<5, [1,4,6,4,1]))

"""filterfalse"""
# Filtra elementos de un iterable, es lo inverso de la función filter
filterfalse = list(itertools.filterfalse(lambda x: x%2, range(10)))
filtering = list(filter(lambda x: x%2, range(10)))

"""groupby"""
# Devuelve una tupla (elemento, grupo_del_elemento) 
groupby = list(itertools.groupby("AABBCDDASBG"))
groupby_1 =  [k for k, g in itertools.groupby('AAAABBBCCDAABBB')]
groupby_2 = [list(g) for k, g in itertools.groupby('AAAABBBCCD')]

"""islice"""
# Devuelve los elemento seleccionados en una lista (start, stop, step)
islice =  list(itertools.islice('ABCDEFG', 2, None, 2))

"""pairwise"""
#  Devuelve una tupla de pares de una posicion con su siguiente 
pairwise = list(itertools.pairwise('ABCDEFG'))


"""starmap"""
# Recibe una funcion y un iterable y devuelve la funcion ejecutada a cada elemento de ese iterable. Es equivalente a map()
starmap =  list(itertools.starmap(pow, [(2,5), (3,2), (10,3)]))
mapping = list(map(pow, [2,3,10], [5,2,3]))


"""zip_longest"""
# Mezcla dos iterables elemento a elemento con la longitud mas grande, lo contrario a zip que se basa en la longitud mas pequeña
zip_longest = list(itertools.zip_longest('ABCDE', 'xy', fillvalue='-'))
zipping = list(zip('ABCDE', 'xy'))


"""Combinatoric iterators"""#-----------------------------------------------------------------------------------------------------------------------------
"""product"""
# Devuelve la combinacion de todos los valores.
product = list(itertools.product([1,2,3], repeat=2))
another_product = [(x,y) for x in "ABC" for y in "ABC"] # Es lo mismo

"""permutations"""
# Devuelve las permutaciones, todos los ordenamientos posibles, sin elementos repetidos
permutations = list(itertools.permutations("ABC", 2))
another_permutations = [(x,y) for x in "ABC" for y in "ABC" if x != y] # Es lo mismo

"""combinations"""
# En orden ordenado, sin elementos repetidos
combinations = list(itertools.combinations('ABCD', 2))

"""combinations_with_replacement"""
# Devuelve subsecuencias de r longitud de elementos del iterable de entrada permitiendo que elementos individuales se repitan más de una vez.
combinations_with_replacement = list(itertools.combinations_with_replacement('ABCD', 2))






"""------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
import more_itertools 

"""Grouping"""#-------------------------------------------------------------------------------------------------------------------------------------------------

"""chunked"""
# Divide un iterador segun la longitud que le pasemos
chunked = list(more_itertools.chunked([1, 2, 3, 4, 5, 6], 3))
chunked_string = list(more_itertools.chunked("Elon Musk", 3))


"""ichunked"""
# FUnciona como el anterior divide un iterable en porciones
ichunked = more_itertools.ichunked(itertools.count(), 4)
c_1, c_2, c_3 = list(next(ichunked)), list(next(ichunked)), list(next(ichunked))

"""chunked_even"""
# Divida iterable en listas de aproximadamente longitud n. Los elementos se distribuyen de manera que las longitudes de las listas difieran en como máximo 1 elemento.
chunked_even = list(more_itertools.chunked_even([1,2,3,4,5,6,7], 3))

"""sliced"""
# Divide el iterable segun la longitud que se le pase
sliced = list(more_itertools.sliced((1, 2, 3, 4, 5, 6), 3))


"""constrained_batches"""
# Produce lotes de elementos iterables con un tamaño combinado limitado por max_count
constrained_batches = list(more_itertools.constrained_batches([b'12345', b'123', b'12345678', b'1', b'1', b'12', b'1'], 10, max_count = 3))


"""distribute"""
# Distribuye la cantidad de elementos segun la cantidad de variables
group_1, group_2, group_3 = more_itertools.distribute(3, [1, 2, 3, 4, 5, 6])
children = more_itertools.distribute(3, [1, 2, 3, 4, 5, 6, 7])


"""divide"""
# Divida los elementos iterables en n partes, manteniendo el orden.Si la longitud del iterable no es divisible por n, entonces la longitud de los iterables devueltos no será idéntica. Si la longitud del iterable es menor que n, los últimos iterables devueltos estarán vacíos
group_1, group_2 = more_itertools.divide(2, [1, 2, 3, 4, 5, 6])
children = more_itertools.divide(3, [1, 2, 3, 4, 5, 6, 7])

"""split_at"""
# Divide un iterable segun la funcion que se le indique, puede o no quedarse con los separadores y puede  regularse la cantidad de separaciones que se desee
split_at = list(more_itertools.split_at('abcdcba', lambda x: x == 'b', maxsplit = 3, keep_separator = True))
split_at_number = list(more_itertools.split_at("one1two2", lambda x: x.isdigit(), maxsplit = 4, keep_separator = True))

"""split_before"""
# Cada division se produce antes de que se cumpla la funcion dada
split_before = list(more_itertools.split_before(range(10), lambda n: n % 2 == 0, maxsplit=2)) 
split_before_strig = list(more_itertools.split_before("abcdefg", lambda n: n == "c" or n == "f"))

"""split_after"""
# Cada division se produce despues de que se cumpla la funcion dada
split_after = list(more_itertools.split_after(range(10),lambda n: n % 3 == 0, maxsplit=2))
split_after_isdigit = list(more_itertools.split_after('one1two2', lambda s: s.isdigit()))

"""split_into"""
# Se le pasa un iterable y una lista de dimesiones para que devuelva el iterable separado segun cada dimension
split_into = list(more_itertools.split_into([1,2,3,4,5,6], [1,2,3]))

"""split_when"""
# Divide el iterable cuando se cumple la funcion que se le pasa
split_when =  list(more_itertools.split_when([1, 2, 3, 3, 2, 5, 2, 4, 2], lambda x, y: x > y, maxsplit = 2))

"""unzip"""
letters, numbers = list(more_itertools.unzip([('a', 1), ('b', 2), ('c', 3), ('d', 4)]))


"""batched"""
# Divide el iterable segun la longitud que se le pase, la ultima pues estar incompleta
batched = list(more_itertools.batched('ABCDEFG', 3))
print(batched)

"""grouper"""
# Agrupa los elementos del iterable segun la longitud que se le pasa y si faltan elementos se puede completa (fill) o no(ignore). Strict da error si el resto de la division de la longitud entre el tamaño que se le pasa da igual a 1. 
grouper = list(more_itertools.grouper('ABCDEFG', 3, incomplete='fill', fillvalue='x'))
grouper_ignore = list(more_itertools.grouper('ABCDEFG', 3, incomplete='ignore', fillvalue='x'))
grouper_strict = list(more_itertools.grouper('ABCDEFGH', 2, incomplete='strict'))

"""partition"""
# Divide el iterable en 2 tuplas, una donde la funcion que se le pase se cumpla y otra en donde no.
part_1, part_2 = list(more_itertools.partition(lambda x: x % 2 != 0, range(10)))


"""transpose"""
# Intercambia las filas por columnas
transpose = list(more_itertools.transpose([(1, 2, 3), (11, 22, 33)]))



"""Lookahead and lookback"""#----------------------------------------------------------------------------------------------------------------------------------------------------
"""spy"""
# Devuelve tuplas unas que contienen las posiciones y otra que lo contiene de manera integra. EL numero que se le pasa es la cantidad de elementos que se require consultar.
(first, second), iterable = more_itertools.spy("abcdefg", 2)

head, iterable = more_itertools.spy([1,2,3,4,5], 3)


"""peekable"""
# Conviente al iterable en un objeto al que se le pueve visualizar la primera posicion con el metodo peek() y se le puede agregar elementos antes con prepend()
peekable = more_itertools.peekable(['a', 'b'])
peekable.prepend("x","w", "z")
#print(peekable.peek(default = "vacío"))

"""seekable"""
# Permite ver el iterable hacia adelante y hacia atrás Va guargando en cache los elementos que se han vidualizado
seekable = more_itertools.seekable((str(n) for n in range(20)))
# Visualiza el iterable a partir del valor que se le introduzca
seekable.seek(10)
# Devuelve un SequenceView() donde se ven todos los elementos que se han visto, (almacenados en cache) 
print(seekable.elements())
# Perimte visualizar los elementos a partir la posicion relativa que se le introduzca
seekable.relative_seek(-2)

#print(seekable.peek(default="empty"))



"""Windowing"""#----------------------------------------------------------------------------------------------------------------------------------------------------------------

"""windowed"""
# Devuelve un sliding window de tamaño n al iterable que se le pase 
windowed = list(more_itertools.windowed([1, 2, 3, 4, 5], 2))


"""substrings"""
# Devuelve todos los subconjuntos del iterable
substrings =  list(more_itertools.substrings("more"))
substrings_list =  list(more_itertools.substrings([1,2,3,4]))

"""substrings_indexes"""
# Devuelve tuplas con todos los subconjuntos del iterable, el indice donde empieza y donde termina
substrings_indexes = list(more_itertools.substrings_indexes("more"))


"""windowed_complete"""
# Devuelve todas las tuplas de sliding window (beginning, middle, end)
windowed_complete = list(more_itertools.windowed_complete(range(7), 3))


"""Augmenting"""#---------------------------------------------------------------------------------------------------------------------------------------------------------------





































