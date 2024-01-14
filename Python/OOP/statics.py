from typing import Self
from datetime import date

# Un método de clase es un método que está vinculado a la clase y no al objeto de la clase. Tienen acceso al estado de la clase, ya que requiere un parámetro de clase que apunta a la clase y no a la instancia del objeto. Puede modificar el estado de una clase que se aplicaría en todas las instancias de la clase.

# staticmethod es un decorador que nos permite usar una funcion dentro de una clase sin que esta reciba argumentos. Este decorador permite llamar a una clase, aunque esta aun no haya sido convertida en un objeto. 

class Calculator:
    def __init__(self, version : int) -> None:
        self.version = version 

    def description(self) -> None:
        print(f"Currently running Calculator on version: {self.version}")
    
    @staticmethod
    def add_number(*numbers: float) -> float:
        return sum(numbers)


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name 
        self.age = age 

    def description(self) -> str:
        return f"{self.name} is {self.age} years old"

    @classmethod 
    def age_from_year(cls, name: str, birth_year: int) -> int:
        if birth_year > 1900:
            current_year: int = date.today().year 
            age: int = current_year - birth_year 
        elif birth_year > 120:
            age = f"Incorrect age: {birth_year} "
        else:
            age = birth_year

        return cls(name, age)
        
if __name__ == "__main__":
    print(Calculator.add_number(1,2,3,4,5,6))
    federico = Person.age_from_year("Guille", 2000)
    print(federico.description())

