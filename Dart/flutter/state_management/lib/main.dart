import 'package:flutter/material.dart';
import 'package:state_management/state_managemente/main_state_management.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: MainStateManagement(),
    );
  }
}
