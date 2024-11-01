void main() {
    for (int i = 0; i < 10; i++) {
        print('$i');
    }

    List<int> scores = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10];
    for (int score in scores) {
        print(score);
    }

    for (int i = 0; i < scores.length; i++) {
        if (scores[i] > 80) {
            continue;
        }
        print(scores[i]);
    }

    for (int score in scores.where((score) => score > 80)) {
        print(score);
    }

    scores.forEach((score) => print(score));

    scores.map((score) => print(score));
}