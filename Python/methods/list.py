lista = [1,2,3]

"""append"""
# Añadir un elemento al final de la lista

lista.append(4)

"""extend"""
# Agregar más de un elemento al final de la lista
lista.extend([5,6,7])

"""insert"""
# Insertar en una posicion un elemento
lista.insert(2, "insert")

"""pop"""
# Eliminar un elemento de atrás hacia adelante segun el posicion que se le introduzca  
lista.pop(4) # lista.pop() == lista[:-1]

"""remove"""
# Eliminar un elemento de adelante hacia atrás
lista.remove(2)

"""reverse"""
# Reversa a la lista
lista.reverse() # == lista[::-1]

"""clear"""
# Elimina la lista completa
lista.clear()
