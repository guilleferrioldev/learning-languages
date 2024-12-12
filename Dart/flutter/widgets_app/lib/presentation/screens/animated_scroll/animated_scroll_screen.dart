import 'package:flutter/material.dart';
import 'dart:math';

class AnimatedScrollScreen extends StatefulWidget {
  static const String name = 'animated_scroll_screen';
  const AnimatedScrollScreen({super.key});

  @override
  State<AnimatedScrollScreen> createState() => _AnimatedScrollScreenState();
}

class _AnimatedScrollScreenState extends State<AnimatedScrollScreen> {
  double _height = 200;
  double _width = 100;
  Color _color = Colors.blue;
  double _borderRadius = 20;

  void _changeSquare() {
    final random = Random();
    setState(() {
      _color = Color.fromRGBO(random.nextInt(255), random.nextInt(255),
          random.nextInt(255), random.nextDouble());
      _width = random.nextInt(300) + 120;
      _height = random.nextInt(300) + 120;
      _borderRadius = random.nextInt(100) + 20;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Animated'),
      ),
      body: Center(
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 400),
          curve: Curves.easeOutCubic,
          width: _width <= 0 ? 0 : _width,
          height: _height <= 0 ? 0 : _height,
          decoration: BoxDecoration(
            color: _color,
            borderRadius: BorderRadius.circular(_borderRadius),
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
          onPressed: () {
            _changeSquare();
          },
          child: const Icon(Icons.play_arrow_rounded)),
    );
  }
}
