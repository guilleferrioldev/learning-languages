import 'package:flutter/material.dart';

class AppTheme {
  ThemeData getTheme() {
    const seedColor = Colors.deepPurple;

    return ThemeData(
      colorSchemeSeed: seedColor,
      useMaterial3: true,
      listTileTheme: const ListTileThemeData(
        iconColor: seedColor,
      ),
    );
  }
}
