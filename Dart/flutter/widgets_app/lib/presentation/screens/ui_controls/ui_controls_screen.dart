import 'package:flutter/material.dart';

class UiControlsScreen extends StatelessWidget {
  static const String name = 'ui_controls_screen';
  const UiControlsScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Ui Controls'),
      ),
      body: const _UiCrontrolsView(),
    );
  }
}

enum Transportation { car, plane, boat, submarine }

class _UiCrontrolsView extends StatefulWidget {
  const _UiCrontrolsView();

  @override
  State<_UiCrontrolsView> createState() => _UiCrontrolsViewState();
}

class _UiCrontrolsViewState extends State<_UiCrontrolsView> {
  bool _isDeveloper = true;
  Transportation selectedTransportation = Transportation.car;
  bool wantsBreakfast = true;

  void _changeDeveloperState() {
    setState(() {
      _isDeveloper = !_isDeveloper;
    });
  }

  void _changeTransportation(Transportation transportation) {
    setState(() {
      selectedTransportation = transportation;
    });
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      physics: const ClampingScrollPhysics(),
      children: [
        SwitchListTile(
            value: _isDeveloper,
            title: const Text("Developer Mode"),
            subtitle: const Text("Controles adicionales"),
            onChanged: (value) {
              _changeDeveloperState();
            }),
        ExpansionTile(
          title: const Text("Transport"),
          subtitle: Text("$selectedTransportation"),
          children: [
            ...Transportation.values.map((transportation) => RadioListTile(
                  value: transportation,
                  groupValue: selectedTransportation,
                  onChanged: (value) {
                    _changeTransportation(value as Transportation);
                  },
                  title: Text(transportation.name),
                  subtitle: Text("Travel by ${transportation.name}"),
                )),
          ],
        ),
        CheckboxListTile(
          value: wantsBreakfast,
          title: const Text("¿Desayuno?"),
          onChanged: (value) {
            setState(() {
              wantsBreakfast = !wantsBreakfast;
            });
          },
        ),
      ],
    );
  }
}
