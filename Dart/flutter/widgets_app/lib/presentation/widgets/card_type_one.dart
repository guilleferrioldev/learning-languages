import 'package:flutter/material.dart';

class CardTypeOne extends StatelessWidget {
  final String label;
  final double elevation;
  const CardTypeOne({super.key, required this.label, required this.elevation});

  @override
  Widget build(BuildContext context) {
    return Card(
        elevation: elevation,
        shape: const RoundedRectangleBorder(
          side: BorderSide(color: Colors.black),
          borderRadius: BorderRadius.all(Radius.circular(10)),
        ),
        child: Padding(
          padding: const EdgeInsets.fromLTRB(10, 5, 10, 10),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(label),
              const Icon(Icons.more_vert),
            ],
          ),
        ));
  }
}
