dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = dict(c=3, d= 4, e= 5)
dict_3 = dict([["f", 6], ["g", 7], ["k", 8]])

"""indexing"""
# Cambia el valor de la clave 

dict_1["a"] = 25 

"""get"""
# dict.get(key[, default])
# DEvuelve el valor de la clave que se le pasa al diccionario y si no existe devuelve un error 

get = dict_1.get("a")

"""items"""
# dict.items()
# Devuelve una nueva vista de los elementos del diccionario (pares (clave, valor)). 

items = dict_1.items()

for k, v in items:
    pass # print(k, v)

"""keys"""
# dict.keys() 
# Devuelve una nueva vista de todas las llaves del diccionario 

keys = dict_1.keys()

"""pop"""
# dict.pop(key[, default])
# Elimina el par (clave, valor) segun la clave que se le pase. Si no lo encuentra, lanza un error. Devuelve el valor de dicha clave

pop = dict_1.pop("b")

"""popitem"""
# dict.popitem()
# Elimina el último par (clave, valor). Si el diccionario está vació, lanza un error. Devuelve el par (clave,valor) que se encontraba al final

popitem = dict_1.popitem()

"""reversed"""
# reversed(dict.items())
# Devuelve un iterado segun lo que se le pase

reverse = list(reversed(dict_2.keys()))
reverse_1 = list(reversed(dict_2.values()))
reverse_2 = dict(reversed(dict_2.items()))

"""setdefault"""
# setdefault(key[, default])
# Si la clave está en el diccionario, devuelve su valor. De lo contrario, inserte la clave con un valor predeterminado y devuelva el valor predeterminado. El valor predeterminado es None.

setdefault = dict_3.setdefault("f")
setdefault_1 = dict_3.setdefault("n", 1)


"""update"""
# dict.update(other_dict)
# Mezclar 2 diccionarios

dict_2.update(dict_3)
x = dict_1 | dict_3
dict_1 |= dict_3 # x == dict (True)


class CustomDict(dict):
    def __add__(self, other):
        self |= other
        return self | other


a = CustomDict({"a":1, "b": 2, "c": 3})
b = CustomDict({"d":4, "e": 5, "f": 6})

z = a + b

print(a==z)
