class Box<T> {
 T value;

 Box(this.value);

 void printValue() {
  print(value);
 }
}

void main() {
 final box = Box<int>(10);
 box.printValue();

 final box2 = Box<String>("Hello");
 box2.printValue();
}