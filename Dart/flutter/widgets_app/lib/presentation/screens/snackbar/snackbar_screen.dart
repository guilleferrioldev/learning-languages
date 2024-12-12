import 'package:flutter/material.dart';

class SnackbarScreen extends StatelessWidget {
  static const String name = 'snackbar_screen';
  const SnackbarScreen({super.key});

  void showSnackBar(BuildContext context) {
    final snackBar = SnackBar(
      content: const Text('Snackbar'),
      duration: const Duration(seconds: 2),
      action: SnackBarAction(
        label: 'Action',
        onPressed: () {},
      ),
    );

    ScaffoldMessenger.of(context).clearSnackBars();
    ScaffoldMessenger.of(context).showSnackBar(snackBar);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Snackbars y diálogos'),
      ),
      body: const _DialogView(),
      floatingActionButton: FloatingActionButton.extended(
          icon: const Icon(Icons.remove_red_eye_outlined),
          onPressed: () {
            showSnackBar(context);
          },
          label: const Text("Mostrar Snackbar")),
    );
  }
}

class _DialogView extends StatelessWidget {
  const _DialogView();

  void openDialog(BuildContext context) {
    showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: const Text("Estás Seguro?"),
            content: const Text("Contenido del diálogo"),
            actions: [
              TextButton(
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                  child: const Text("Cancelar")),
              FilledButton(
                  onPressed: () {
                    Navigator.of(context).pop();
                  },
                  child: const Text("Aceptar")),
            ],
          );
        });
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          FilledButton.tonal(
              onPressed: () {
                showAboutDialog(context: context, children: [
                  const Text("Licencias usadas"),
                ]);
              },
              child: const Text("Licencias usadas")),
          const SizedBox(
            height: 20,
          ),
          FilledButton.tonal(
              onPressed: () {
                openDialog(context);
              },
              child: const Text("Mostrar diálogo")),
        ],
      ),
    );
  }
}
