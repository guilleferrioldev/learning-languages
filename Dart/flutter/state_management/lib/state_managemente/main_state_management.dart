import 'package:flutter/material.dart';
import 'package:state_management/state_managemente/dont/login_page.dart'
    as dont;
import 'package:state_management/state_managemente/no_package/login_page.dart'
    as no_package;
import 'package:state_management/state_managemente/package/login_page.dart'
    as package;

class MainStateManagement extends StatelessWidget {
  const MainStateManagement({super.key});

  void _onPressed(BuildContext context, Widget child) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (_) => child,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    const separator = SizedBox(height: 20);
    return Scaffold(
      appBar: AppBar(
        title: Text("State management"),
      ),
      body: ListView(
        padding: const EdgeInsets.all(40),
        children: [
          FilledButton(
              onPressed: () => _onPressed(context, dont.LoginMainPage()),
              child: Text("Don't do this")),
          separator,
          FilledButton(
              onPressed: () => _onPressed(context, no_package.LoginMainPage()),
              child: Text("Without any package")),
          separator,
          FilledButton(
              onPressed: () => _onPressed(context, package.LoginMainPage()),
              child: Text("With package")),
        ],
      ),
    );
  }
}
