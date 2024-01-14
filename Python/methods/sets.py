set_1 = {1,2,3}
set_2 = frozenset({1,2,3,4,5,6})
set_3 = {3,4,5}

"""isdisjoint"""
# set.isdisjoint(other)
# Devuelve True si el conjunto no tiene elementos en común con otros. Los conjuntos son disjuntos si y sólo si su intersección es el conjunto vacío.

isdisjoint = set_1.isdisjoint(set_2)

"""issubset"""
# set.issubset(other)
# Devuelve True si un conjunto en subconjunto de otro

issubset = set_1.issubset(set_2) 
issubset_2 = set_1 <= set_2

"""issuperset"""
# set.issubset(other)
# Devuelve True si un conjunto en superconjunto de otro

issuperset = set_2.issuperset(set_1)
issuperset_2 = set_2 >= set_1

"""union"""
# set.union(other)
# Une un conjunto con otros

union = set_1.union(set_2) 
union_2 = set_1 | set_2

"""intersection"""
# set.intersection(other)
# Devuelve la intersección de ambos conjuntos

intersection = set_1.intersection(set_2)
intersection_2 = set_1 & set_2 

"""difference"""
# set.difference(other)
# Devuelve la diferencia entre ambos conjuntos 

difference = set_2.difference(set_1)
difference_2 = set_2 - set_1 

"""symmetric_difference"""
# set.symmetric_difference(other)
# Devuelve la diferencia simetrica entre ambos conjuntos 

symmetric_difference = set_1.symmetric_difference(set_2)
symmetric_difference_2 = set_2 ^ set_1 


"""update"""
# Añadir múltiples elementos de otro conjunto que no se encuentren en el primero 

set_1.update(set_3) # set_1 |= set_3

"""intersection_update"""
# Mantiene los elementos de la intersección y los que estan en el propio conjunto

set_1.intersection_update(set_2) # set_1 &= set_2

"""difference_update"""
# Mantiene los elementos que no se encuentran en el otro conjunto

set_1.difference_update(set_3) # set_1 -= set_2

"""symmetric_difference_update"""
# Mantiene los elementos de la diferencia simétrica

set_1.symmetric_difference_update(set_2) 

"""add"""
# Añade un elemento al conjunto

set_1.add(7)

"""remove"""
# Elimina un elemento del conjunto pero lanza un error si este no existe

set_1.remove(3)

"""discard"""
# Elimina un elemento del conjunto pero no lanza error

set_1.discard(1)

"""pop"""
# Elimina un elemento arbitrario de un conjunto 

set_1.pop()

"""clear"""
# Elimina todos los elementos

set_1.clear()
