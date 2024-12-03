import 'package:flutter/material.dart';

class CounterScreen extends StatefulWidget {
  const CounterScreen({super.key});

  @override
  State<CounterScreen> createState() => _CounterScreenState();
}

class _CounterScreenState extends State<CounterScreen> {
  int clickCounter = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Center(child: Text("Counter Screen")),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text('$clickCounter',
                  style: const TextStyle(
                      fontSize: 160, fontWeight: FontWeight.w100)),
              Text('Click${clickCounter == 1 ? '' : 's'}',
                  style: const TextStyle(fontSize: 25)),
            ],
          ),
        ),
        floatingActionButton: Column(
          mainAxisAlignment: MainAxisAlignment.end,
          children: [
            CustomFloatingActionButton(
              icon: Icons.refresh_rounded,
              onPress: () {
                setState(() {
                  clickCounter = 0;
                });
              },
            ),
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 15),
              child: CustomFloatingActionButton(
                icon: Icons.plus_one,
                onPress: () {
                  setState(() {
                    clickCounter++;
                  });
                },
              ),
            ),
            CustomFloatingActionButton(
              icon: Icons.exposure_minus_1_outlined,
              onPress: () {
                setState(() {
                  if (clickCounter > 0) {
                    clickCounter--;
                  }
                });
              },
            ),
          ],
        ));
  }
}

class CustomFloatingActionButton extends StatelessWidget {
  final IconData icon;
  final VoidCallback onPress;
  const CustomFloatingActionButton({
    super.key,
    required this.icon,
    required this.onPress,
  });

  @override
  Widget build(BuildContext context) {
    return FloatingActionButton(
        shape: const CircleBorder(), onPressed: onPress, child: Icon(icon));
  }
}
