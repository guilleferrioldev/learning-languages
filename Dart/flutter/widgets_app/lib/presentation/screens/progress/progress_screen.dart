import 'package:flutter/material.dart';

class ProgressScreen extends StatelessWidget {
  static const String name = 'progress_screen';
  const ProgressScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('ProgressIndicator'),
      ),
      body: const _ProgressView(),
    );
  }
}

class _ProgressView extends StatelessWidget {
  const _ProgressView();

  @override
  Widget build(BuildContext context) {
    return const Center(
        child: Column(children: [
      SizedBox(
        height: 30,
      ),
      Text('Circular progress indicator'),
      SizedBox(
        height: 20,
      ),
      CircularProgressIndicator(
        strokeWidth: 2,
        backgroundColor: Colors.black45,
      ),
      SizedBox(
        height: 20,
      ),
      Text('Circular y linear controlado'),
      SizedBox(
        height: 20,
      ),
      _ControllerProgressInicator()
    ]));
  }
}

class _ControllerProgressInicator extends StatelessWidget {
  const _ControllerProgressInicator();

  @override
  Widget build(BuildContext context) {
    return StreamBuilder<Object>(
        stream: Stream.periodic(const Duration(milliseconds: 300), (value) {
          return (value * 2) / 100;
        }).takeWhile((value) => value < 100),
        builder: (context, snapshot) {
          final double progressValue =
              snapshot.hasData ? snapshot.data as double : 0.0;

          return Padding(
              padding: const EdgeInsets.symmetric(horizontal: 20),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  CircularProgressIndicator(
                    value: progressValue,
                    strokeWidth: 5,
                    backgroundColor: Colors.black12,
                  ),
                  const SizedBox(
                    width: 20,
                  ),
                  Expanded(
                      child: LinearProgressIndicator(
                          value: progressValue,
                          backgroundColor: Colors.black12))
                ],
              ));
        });
  }
}
