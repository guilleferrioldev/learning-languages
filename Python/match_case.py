var: str = "e"
num: int = 11 

def check_var(variable, number):
    match variable:
        case "a" | "b" as value:
            print(value)
        case "c" as value:
            print(value)
        case value if number <= 10:
            print(value)
        case _:
            print("None of the above")

#check_var(var, num)


my_tuple = (4,5,6,7,3,61,1,2)

def check_tuple(tupl):
    match tupl:
        case (var1, var2, var3):
            print(var1)
        case (_,_,_,_):
            print("A")
        case (1, (2|3) as num, 4, 5):
            print(num)
        case (1,2, *others):
            print(others)
        case (first, *others, 2) | (1, first, *others):
            print(others, first)
        case (*others, 1,2):
            print(others)

# check_tuple(my_tuple)



my_dict = {"key1": 1, "key2": 2, "key3": 2}

def check_dict(dictionary):
    match dictionary:
        case {"key2": value as key2, **others}:
            print(key2,":",value, others)

# check_dict(my_dict)


class Person:
    name = "Juan"
    age = 35 

    __match_args__ = ("name", "age")

person = Person()

match person:
    case Person(name = ("Jack" | "John") as name, age = 35 as age):
        print(name, age)
    case Person(name = "Juan") | Person(name = "John"):
        print("It is a person")
    case Person(name):
        print(name)

























