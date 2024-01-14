# Example 0
def func(x: int) -> int:
    return x + 1
    get_value()

x: int = 9
if w := func(x):
    print(w)

# Example 1
def analyze_text(text:str) -> dict:
    return {"words": (words := text.split()), "amount": len(words), "chars": len(" ".join(words)), "reversed": words[::-1]}

print(analyze_text("Hello World"))

user_input: str = "Hello, world!"

# Example 2
if (text := len(user_input)) > 5:
    print(text, " yes")
else:
    print(text, " no")

# Example 3
def get_value():
    return  

if (var := get_value()):
    print(var)
else: print("No value")


from random import randint
# Example 4 
def add_items(item: str, lst: list = None) -> dict:
    return (w := (lst + [randint(0,item)])) 

print(add_items(5, [2,3,4]))



