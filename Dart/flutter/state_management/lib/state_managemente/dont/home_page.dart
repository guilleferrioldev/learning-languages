import 'package:flutter/material.dart';
import 'package:state_management/state_managemente/dont/menu_page.dart';

class HomePage extends StatefulWidget {
  final ValueChanged<bool> onThemeSelected;
  const HomePage({super.key, required this.onThemeSelected});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int counter = 0;

  void _incrementCounter() {
    setState(() {
      counter++;
    });
  }

  void _decrementCounter() {
    if (counter == 0) return;
    setState(() {
      counter--;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home'),
      ),
      drawer: Drawer(
        child: MenuPage(onThemeSelected: widget.onThemeSelected),
      ),
      body: Center(
        child: Column(
          children: [
            Expanded(
                child: Padding(
                    padding: const EdgeInsets.all(20),
                    child: Row(
                      children: [
                        Expanded(
                            child: InkWell(
                          onTap: _incrementCounter,
                          child: FittedBox(
                            child: Text('+'),
                          ),
                        )),
                        Expanded(
                            child: InkWell(
                          onTap: _decrementCounter,
                          child: FittedBox(
                            child: Text('-'),
                          ),
                        ))
                      ],
                    ))),
          ],
        ),
      ),
      bottomNavigationBar: SizedBox(
        height: 100,
        child: TotalWidget(counter: counter),
      ),
    );
  }
}

class TotalWidget extends StatelessWidget {
  final int counter;
  const TotalWidget({super.key, required this.counter});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.blue,
      height: 100,
      child: Padding(
          padding: const EdgeInsets.all(20),
          child: FittedBox(
            child: Text(
              '$counter',
              style: const TextStyle(fontSize: 30),
            ),
          )),
    );
  }
}
