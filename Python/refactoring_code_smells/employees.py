"""
#1: imprecise types (Enum)
#2: duplicate code (Delete equal functions)
#3: not using available built-in functions (Use list comprehension and other python functions)
#4: vague identifiers (Correct name of variables)
#5: using isinstance to separate behavior 
#6: using boolean flags to make a method do 2 different things (Dont pass booleans as arguments in functions )
#7: catching and then ignoring exceptions (Dont use pass in exception)
"""

from dataclasses import dataclass, field 
from typing import List
from enum import Enum, auto
from abc import ABC, abstractmethod

FIXED_VACATION_DAY_PAYOUT = 5 

class Role(Enum):
    "Employee roles"
    
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()

@dataclass
class Employee(ABC):
    name: str
    role: Role
    vacation_days: int = 25

    def take_a_holiday(self) -> None:
        """Let the employee take a single holiday"""

        if self.vacation_days < 1:
            raise ValueError(
                        "You don't have any holidays left. Now back to work, you!"
                        )
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")
    
    def payout_a_holiday(self):
        """Let the employee get paid for unused holidays"""
        
        # check that there are enough vacation days left for a payout
        if self.vacation_days < FIXED_VACATION_DAY_PAYOUT:
            raise ValueError(
                        f"You don't have enough holidays left over for a payout.\
                        Remaining holidays : {self.vacation_days}"
                        )

        self.vacation_days -= FIXED_VACATION_DAY_PAYOUT 
        print(f"Paying out a holiday left: {self.vacation_days}")

    @abstractmethod
    def pay(self) -> None:
        """Meyhod to call when paying an employee"""

@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours"""

    hourly_rate_in_dollars: float = 50 
    hours_worked: int = 10 
    
    def pay(self):
        print(f"Paying employee {employee.name} a hourly rate of \
            ${employee.hourly_rate_in_dollars} for {employee.hours_worked} hours"
                )

@dataclass
class SalaryEmployee(Employee):
    """Employee that's paid based on number of worked hours"""
    
    monthly_salary_in_dollars: float = 5000 
    
    def pay(self):
        print(f"Paying employee {self.name} a monthly salary of ${self.monthly_salary_in_dollars}")


@dataclass
class Company:
    """Represents a company with empleyees"""
    employees: List[Employee] = field(default_factory = list)

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of empleyees"""
        self.employees.append(employee)
    
    def find_employees(self, role: Role) -> List[Employee]:
        """Find all maanger empleyees"""
        return [employee for employee in self.employees if employee.role == role]
 
def main() -> None:
    "Main function"

    company = Company()

    company.add_employee(SalaryEmployee(name = "Louis", role = Role.MANAGER))
    company.add_employee(HourlyEmployee(name = "Brenda", role = Role.PRESIDENT))
    company.add_employee(HourlyEmployee(name = "Tim", role = Role.INTERN))

    print(company.find_employees(Role.PRESIDENT))
    print(company.find_employees(Role.MANAGER))
    print(company.find_employees(Role.INTERN))
    company.employees[0].pay()
    company.employees[0].take_a_holiday()


if __name__ == "__main__":
    main()
