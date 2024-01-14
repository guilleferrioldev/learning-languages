"""abs"""
# abs()
# Absolute value

class ImplementedAbs:
    def __init__(self, string):
        self.string = string 

    def __abs__(self):
        return self.string.lower()

custom_obj = ImplementedAbs("Hello")

x = abs(-9)
y = abs(custom_obj)


"""aiter and anext"""
# aiter(async_iterable)
# anext(async_iterator)
# Asynchronous iterator
import asyncio 

class AsyncIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop 

    def __aiter__(self):
        self.current = self.start
        return self 

    async def __anext__(self):
        await asyncio.sleep(1)
        if self.current >= self.stop:
            raise StopAsyncIteration

        self.current += 1 
        return self.current -1

async def example_aiter():
    custom_obj = AsyncIterator(1,10)
    obj_iter = aiter(custom_obj)
    print(obj_iter)
    async for num in obj_iter:
        print(num)

async def example_anext():
    custom_obj = AsyncIterator(1,10)
    obj_iter = aiter(custom_obj)
    print(await anext(obj_iter))
    print(await anext(obj_iter))
    print(await anext(obj_iter))

#asyncio.run(example_aiter())
#asyncio.run(example_anext())


"""all"""
# all(iterable)
# If all elements are True 

true_all = all(["a", 1, [3], [1,2], True]) # -> True

false_all = all(["", 0, [], [0,0], False])

"any" 
# any(iterable)
# If all of the values are True

true_any = any(["a", 0, [], [0,0], False])

false_any = any([ 0, [], "", False]) 


"""bin"""
# bin(number)
# Binary representation of an integer 

base10 = 100 
base2 = bin(base10) 

base10_neg = -100 
base2_neg = bin(base10_neg) 


"""callable"""
# callable(object)
# Return True or False if something is calable

class Class:
    pass 

def func():
    print("hi")

def func2():
    def inner():
        pass 
    return inner 


func3 = lambda x: x + 1 
not_func = "hello"


c = callable(Class) # -> True
f1 = callable(func) # -> True
f2 = callable(func2()) # -> True
f3 = callable(func3) # -> True
nf = callable(not_func) # -> False


"""chr"""
# chr(number)
# Return the caracter that is represented with the number

A = chr(65) 
a = chr(97)


"""complex"""
# complex(real, img)
# Complex number 

complex1 = complex("32+2j")
complex2 = complex(3, 4)


"""delattr"""
# delattr(object, name)
# Delete attributes from a class

class MyClass:
    def __init__(self, x):
        self.x = x 

my_class = MyClass(4)
 
#delattr(my_class, "x") # is equal than == del my_class.x 
#print(my_class.x) # -> AttributeError: 'MyClass' object has no attribute 'x' 


"""dir"""
# dir(object)
# Is gonna give me everything inside the package or an object
import math

dir_math = dir(math)

dir_class = dir(my_class)


"""divmod"""
# divmod(a, b)
# Division Modulo 

quotient, remainder = divmod(10,3) # -> 3 1


"""enumerate"""
# enumerate(iterable, start = 0)
# Access the index and the value in an iterable object 

values = ["a", "b", "c", "d"]

def enumerating(iterable):
    for index, value in enumerate(iterable):
        print(f"{index} : {value}") 


"""eval"""
# eval(expression[, globals[, locals]])
# Evaluation if an expression is correct

#code = input("enter some code: ") # code : print("x") -> x
#eval(code)


"""exec"""
# exec(expression[, globals[, locals]])
# Ejecuta el codigo, ademas de evaluar si es cierto. Se pueden hacer mas de una operacion 

#code = input("enter some code: ") # code: x = 0; x+=1; print(x) -> 1
#exec(code)


"""frozenset"""
# frozenset(iterable)
# Inmutable version of the set

lst = [1,2,3]
s = set(lst)
s.add(4)

fs = frozenset(s)


"""getattr"""
# getattr(oject, name)
# Get attributes from a class 

# my_class was implemented before
x = getattr(my_class, "x")



"""globals"""
# globals()
# Return all global variables

globals()

"""hasattr"""
# hasattr(object, name)
# Return True or False if the attribute exists

# my_class was implemented before

h_t = hasattr(my_class, "x")
h_f = hasattr(my_class, "y")


"""hash"""
# hash(object)
# Is used expecificaly for inmutable objects 

string_hash = hash("randomstring")
num_hash = hash((1,2))


"""hex"""
# hex(number)
# Is gonna give you the hexadecimar representation of an integer

class CustomHex:
    def __index__(self):
        return 10 


h1 = hex(255) # -> 0xff

custom_hex = CustomHex()
h2 = hex(custom_hex) # -> 0xa


"""isinstance"""
# isinstance(object, classinfo)
# Return True or False if the type of the object is correct or not

a = 1 

i = isinstance(a, int) # -> True 

i_t = isinstance(int, type) # -> True


"""issubclass"""
# issubclass(class, classinfo)
# Return True or False if a class is subclass of another class is correct or not


class A:
    pass 

class B(A):
    pass 


sub = issubclass(B, A) # -> True

sub2 = issubclass(A, object) # -> True


"""locals"""
# locals()
# Is gonna give you informations that all of the locals variables that you have access to 

locals()


"""max"""
# max(iterable, key=function)
# max(*args, key=function)

max([3,5,9,-1,2])

max("hello", "world", "yes", key = len)


"""memoryview"""
# memoryview(object)
# How much bytes it use to represent the object

x = b"abcdef"
mem = memoryview(x)


"""min"""
# min(iterable, key=function)
# min(*args, key=function)

min([3,5,9,-1,2])

min("hello", "world", "yes", key = len)


"""object"""
#object()
# Create a new object

empty = object()


"""pow"""
# pow(a, b)

x = pow(10, 2)


"""round"""
# round(number, ndigits)

y = round(10.23456, 2)


"""setattr"""
# setattr(object, name, value)
# Update or create a new attribute on a class

# my_class was implemented before
setattr(my_class, "y", 5)

"""slice"""
# slice(start, stop, step)
# Slice an iterable

lst = [2, 4, 6, 8, 10]
s = slice(1,-1,2)
res = lst[s] # -> [4,8]

"""sum"""
# sum(iterable, start=0)
# Sum all the values in an iterable

x = sum([1, 2, 3, 4, 5], start= 2)


"""vars"""
# vars(object)
# Is gonna give you all of the values ot attributes associate with an especific object ot type

x = vars()
y = vars(list)
z = vars(my_class)


"""zip"""
# zip(*iterables, stric = False)
# Take all of the associate indexes and put them together in a tuple

widths =  [1, 3, 5]
heights = [2, 6, 8]
zipped = list(zip(widths, heights))


