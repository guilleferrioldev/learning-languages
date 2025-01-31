import 'package:flutter/material.dart';

class HomeBloc extends ChangeNotifier {
  int counter = 0;

  void incrementCounter() {
    counter++;
    notifyListeners();
  }

  void decrementCounter() {
    if (counter == 0) return;
    counter--;
    notifyListeners();
  }
}
