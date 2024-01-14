from sys import getsizeof
from functools import reduce

"""Lambda"""
func = lambda x: x + 5

func_2 = lambda x, y = 4: x * y 

"""Map"""
# Toma dos argumentos, una funcion y un iterable y le aplica la funcion a cada elemento del iterable
lista = range(1,11)

def square(x: int) -> int:
    return x**x 

squares = map(lambda x: x**x, lista)
squares_2 = [square(item) for item in lista] # Es lo mismo


"""Filter"""
# Toma una funcion y un iterable y un iterable y filtra todos los valores que devielva veradero
filtering = list(filter(lambda x: x % 2, lista))
mapping = list(map(lambda x: x + 7, filtering))


"""reverser"""
# Revierte un iterables
reversing = list(reversed([1,2,3,4,5])) 


"""Sorted"""
sorting = sorted([3, 4, 22, -9, 2, 44 ,2], reverse = True)
sorting_2 = sorted([[1,2], [-2,3], [4,4], [2,2], [-1,-1]], key = sum)

"""Reduce""" 
# Toma una funcion con dos parametros y un iterable y un iterable y devuelve un valor único
reduced = reduce(lambda x,y: x+y, lista)
