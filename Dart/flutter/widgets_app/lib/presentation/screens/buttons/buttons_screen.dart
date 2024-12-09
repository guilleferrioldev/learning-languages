import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:widgets_app/presentation/widgets/widgets.dart';

class ButtonsScreen extends StatelessWidget {
  static const String name = 'buttons_screen';
  const ButtonsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Botones"),
      ),
      body: const _ButtonsView(),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          context.pop();
          //context.replaceNamed(HomeScreen.name);
        },
        child: const Icon(Icons.arrow_back_ios_rounded),
      ),
    );
  }
}

class _ButtonsView extends StatelessWidget {
  const _ButtonsView();

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      width: double.infinity,
      child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 20),
          child: Wrap(
            spacing: 10,
            alignment: WrapAlignment.center,
            children: [
              ElevatedButton(
                onPressed: () {},
                child: const Text("ElevatedButton"),
              ),
              const ElevatedButton(
                onPressed: null,
                child: Text("Disabled"),
              ),
              ElevatedButton.icon(
                  onPressed: () {},
                  label: const Text("Elevated Icon"),
                  icon: const Icon(Icons.access_alarm_rounded)),
              FilledButton(onPressed: () {}, child: const Text("Filled")),
              FilledButton.icon(
                  onPressed: () {},
                  label: const Text("Filled Icon"),
                  icon: const Icon(Icons.accessibility_new)),
              OutlinedButton(onPressed: () {}, child: const Text("Outlined")),
              OutlinedButton.icon(
                  onPressed: () {},
                  label: const Text("Outlined Icon"),
                  icon: const Icon(Icons.whatshot)),
              TextButton(onPressed: () {}, child: const Text("TextButton")),
              TextButton.icon(
                  onPressed: () {},
                  label: const Text("TextButton Icon"),
                  icon: const Icon(Icons.telegram)),
              IconButton(onPressed: () {}, icon: const Icon(Icons.add)),
              const Custombutton()
            ],
          )),
    );
  }
}
