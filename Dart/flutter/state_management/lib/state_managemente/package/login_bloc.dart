import 'package:flutter/material.dart';

class LoginBloc extends ChangeNotifier {
  bool isDarkMode = false;

  void updateTheme(bool darkMode) {
    isDarkMode = darkMode;
    notifyListeners();
  }
}
