# Avoid endless if-else statements 

def do_one(x):
    return f"one: x+1 = {x+1}"

def do_two(x):
    return f"two: x+2 = {x+2}"

def do_three(x):
    return f"three: x+3 = {x+3}"

def do_default(x):
    return f"default: x = {x}"

x = 1

actions = {1:do_one, 2:do_two, 3:do_three, 4:do_default}

action = actions.get(x, do_default)
print(action(x))









