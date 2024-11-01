void main() {
    List<int> scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10];
    print(scores);
    scores.add(0);
    scores.add(10);
    scores.remove(0);
    scores.removeLast();
    scores.shuffle();
    int index = scores.indexOf(50);
    print(index);
    print(scores);

    final Set<String> names = {"mario", "luigi", "peach"};
    names.add("toad");
    names.remove("luigi");
    names.removeWhere((name) => name.startsWith("p"));
    print(names.length);
    print(names);
}