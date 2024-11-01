void main() {
    Map<String, int> scores = {
        "Mario": 100,
        "Luigi": 90,
        "Peach": 80,
        "Toad": 70,
        "Bowser": 60,
        "Yoshi": 50,
        "Donkey Kong": 40,
        "Kirby": 30,
        "Link": 20,
        "Fox": 10,
    };
    print(scores);
    scores["Toad"] = 10;
    print(scores["Toad"]);

    print(scores.keys);
    print(scores.values);
    print(scores.entries);
    print(scores.containsKey("Toad"));
    print(scores.containsValue(10));
    scores.remove("Toad");
}