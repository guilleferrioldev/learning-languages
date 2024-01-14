from typing import List, Callable

z: Callable[[int, int], int] = lambda x, y: x + y 

Vector = List[float]

def foo(lst: list[float]) -> list[float]:
    return lst[1:]

