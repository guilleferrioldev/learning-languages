"""capitalize"""
# str.capitalize()
# La primera posicion del string (string[0]) en mayuscula y el resto en minúscula

capitalize = "Hello World".capitalize()

"""casefold()"""
# str.casefold()
# Devuelve todas las letras del string en minusculas. Es como .lower() pero entiende caracteres más extraños

casefold = "Hello World".casefold()

"""count"""
# str.count(sub,[ start[, end]])
# Devuelve cuantas veces aparece un valor en determindao rango del string 

count = "Hello World".count("l", 1, 5)

"""endswith"""
# str.endswith(suffix,[ start [, end]])
# Devuelve True o False si el string termina con determinado sufijo

endswith = "Hello World".endswith("Wor", 2, -2)

"""find"""
# str.find(sub[, start[, end]])
# Devuelve la primera posicion donde aparece lo que se busca 

find = "Hello World".find("or", 3, -2)

"""index"""
# str.index(sub[, start[, end]])
# Igual que find pero devuelve un error cuando el valor es no encontrado

index = "Hello World".index("or")

"""isalnum"""
# str.isalnum()
# Devuelve True si hay numeros en la cadena, y no pueden haber espacios  

isalnum = "Hello2World".isalnum()

"""isalpha"""
# str.isalpha()
# Devuelve True si sólo hay letras en la cadena, ni numeros ni espacios

isalpha = "HelloWorld".isalpha()

"""isdigit"""
# str.isdigit()
# Devuelve True si sólo hay numeros en la cadena, ni letras ni espacios  

isdigit = "12345".isdigit()

"""islower"""
# str.islower()
# Devuelve True o False si esta todo en minuscula  

islower = "hello world 1".islower() 

"""isnumeric"""
# str.isnumeric()
# Lo mismo que isdigit

isnumeric = "12345".isnumeric() 

"""isprintable"""
# str.isprintable()
# Devuelve True si no tiene caracteres separadores como \t o \n, etc

isprintable = "Hello World".isprintable() 

"""isspace"""
# str.isspace()
# Devuelve True si solo hay espacios en blace

isspace = "    \n \t ".isspace() 

"""istitle"""
# str.istitle()
# Devuelve True si todos las palabras despues del espacios empiezan con mayuscula y el resto de la palabra está en minuscula, o numero y el resto sigue siendo numero y no letras

istitle = "Hello World 131".istitle()

"""isupper"""
# str.isupper()
# Devuelve True si todo esta en mayuscula o es numeros 

isupper = "HELLO WORLD 111A".isupper()


"""join"""
# separator.join(iterable)

join = "".join(["H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d"])

"""lower"""
# str.lower()
# Devuelve el string en minuscula 

lower = "Hello World".lower()

"""lstrip"""
# str.lstrip()
# Devuelve una copia del string eliminando los caracteres iniciales que se le pase, por defecto tine espacios

lstrip = "    Hello World".lstrip("    Hello")

"""partition"""
# str.partition(sep)
# Parte el string en una tuple de dimension 3, en la que la separa en dependencia del separador que se le pase cuando lo encuentre por primera vez

partition = "Hello World".partition("o")

"""removeprefix"""
# str.removeprefix(prefix)
# Elimina el prefijo que se le pase

removeprefix = "Hello World".removeprefix("He")

"""removesuffix"""
# str.removesuffix(suffix)
# Elimina el sufijo que se le pase

removesuffix = "Hello World".removesuffix("rld")

"""replace"""
# str.replace(old, [new, count])
# Devuelve una copia del string donde se reemplaza lo que se le pide 

replace = "Hello World , Hello".replace("Hello", "Hi", 1)


""""rfind"""
# str.rfind(sub[, start[, end]])
# Devuelve la ultima posicion en la que se encontro lo que se busca

rfind = "Hello World".rfind("o", 3, -1)

"""rindex"""
# str.rindex(sub[, start[, end]])
# Lo mismo que rfind pero lanza un error si no lo encuentra

rindex = "Hello World".rindex("o", 3, -1)

"""rpartition"""
# str.rpartition(sep)
# Parte el string en una tuple de dimension 3, en la que la separa en dependencia del separador que se le pase cuando lo encuentre por ultima vez

rpartition = "Hello World".rpartition("o")


"""rsplit"""
# str.rsplit(sep=None, maxsplit=- 1)
# Devuelve una lista separando en dependencia del separador que se le pase, por defecto tiene espacios en blanco, empezando de atras para adelante

rsplit = "Hello World Hello World".rsplit(sep=None, maxsplit = -1)

"""rstrip"""
# str.rstrip()
# Devuelve una copia del string eliminando los caracteres finales que se le pase, por defecto tine espacios

rstrip = "Hello World    ".rstrip("World    ")

"""split"""
# str.split(sep= None, maxsplit = -1)
# Devuelve una lista separando en dependencia del separador que se le pase, por defecto tiene espacios en blanco, empezando de adelante hacia atras

split = "Hello World Hello World".split(sep=None, maxsplit = -1)


"""splitlines"""
# str.splitlines(keepends=False)
# Divide una lista las lineas de un string, keepends es para mantener o no el simbolo de salto de linea

splitlines = "Hello World".splitlines(keepends = True)


"""startswith"""
# str.startswith(prefix[, start[, end]])
# Devuelve True si el string empieza con determinado prefijo

startswith = "Hello World".startswith("Hel", 0, -2)

"""strip"""
# str.strip([chars])
# Devuelve una copia del string donde elimina al principio y al final lo seleccionado, por defecto están los espacios en blanco 

strip = "    Hello World    ".strip()

"""swapcase"""
# str.swapcase()
# Cambia las letras de mayuscula a minuscula y viceversa 

swapcase = "Hello World".swapcase()

"""title"""
# str.title()
# Devuelve todas las letras despues de un caracter que no sea letra en mayusculas, sin importar si tiene numeros adelante, y el resto de la palabra en minuscula

title = "hello 125wor3ld".title()

"""upper"""
# str.upper()
# Devuelve el string en mayuscula 

upper = "Hello World".upper()


"""zfill"""
# str.zfill(len)
# Relleno con "0" hasta la longitud que se le introduzca. si el prime valor en un "-" entonces rellena a partir del segundo 

zfill = "-42".zfill(5)
