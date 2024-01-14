# Estructura

try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass


# Ejemplos
bad_var = 4

try:
    f = open("test.txt")
    var = bad_var
    if f.name != "test.txt":
        raise Exception
except FileNotFoundError as file:
    print(f"Sorry. This file does not exist {file}")
except NameError as name:
    print(f"Sorry. Something went wrong {name}")
except Exception:
    print("Error!")
else:
    print(var)
    print(f.read())
    f.close()
finally:
    print("Excecuting Finally ...")
