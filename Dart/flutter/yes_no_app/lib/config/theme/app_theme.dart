import 'package:flutter/material.dart';

const Color _customColor = Color(0xFF5c11d4);

const List<Color> _colorThemes = [
  _customColor,
  Colors.blue,
  Colors.teal,
  Colors.green,
  Colors.yellow,
  Colors.orange,
  Colors.pink
];

class AppTheme {
  final int selectedColor;

  AppTheme({this.selectedColor = 0})
      : assert(selectedColor >= 0 && selectedColor < _colorThemes.length,
            "Color Theme not found");

  ThemeData theme() {
    return ThemeData(
        useMaterial3: true,
        brightness: Brightness.light,
        colorSchemeSeed: _colorThemes[selectedColor]);
  }
}
