import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: ListView(
      children: [
        ListTile(
          title: Text('Cubits'),
          subtitle: Text('Cubits are a simple state manager'),
          trailing: Icon(Icons.arrow_forward_ios_rounded),
          onTap: () => {context.push('/cubits')},
        ),
        ListTile(
          title: Text('Bloc'),
          subtitle: Text('Bloc is a composite state manager'),
          trailing: Icon(Icons.arrow_forward_ios_rounded),
          onTap: () => {context.push('/bloc')},
        ),
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 10),
          child: Divider(),
        ),
        ListTile(
          title: Text('New user'),
          subtitle: Text('Form management'),
          trailing: Icon(Icons.arrow_forward_ios_rounded),
          onTap: () => {context.push('/register')},
        ),
      ],
    ));
  }
}
