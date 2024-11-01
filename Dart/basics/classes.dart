class Person {
 String name;
 int age;

 Person(this.name, this.age);

 void greet() {
  print("Hi, my name is $name and I am $age!");
 }
}

class Employee extends Person {
 String? department;

 Employee(String name, int age, String? department)
   : super(name, age) {
  this.department = department;
 }

 // Factory Constructor
 factory Employee.fromPerson(Person person, String? department) {
  return Employee(person.name, person.age, department);
 }

 @override
 void greet() {
  print("Hi, my name is $name, I am $age, and I work in the $department department!");
 }
}

void main() {
 final person = Person("Guille", 24);
 person.greet();

 // Use the factory constructor
 final employee = Employee.fromPerson(person, "IT"); 
 employee.greet();
}
