void main() {
    final greeting = greetWithPositionalParameters("Guille", 24);
    print(greeting);

    final greeting2 = greetWithNamedParameters(age: 24, name: "Guille");    
    print(greeting2);
}

String greetWithPositionalParameters(String name, int age) {
    return "Hi, my name is $name and I am $age!";
}

String greetWithNamedParameters({String? name, required int age}) {
    return "Hi, my name is $name and I am $age!";
}
