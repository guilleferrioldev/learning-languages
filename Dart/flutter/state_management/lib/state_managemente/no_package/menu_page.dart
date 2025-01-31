import 'package:flutter/material.dart';
import 'package:state_management/state_managemente/main_state_management.dart';
import 'package:state_management/state_managemente/no_package/login_page.dart';

class MenuPage extends StatelessWidget {
  const MenuPage({super.key});

  @override
  Widget build(BuildContext context) {
    final logicBloc = MyIngeretedWidget.of(context)!.loginBloc;
    return ListView(padding: const EdgeInsets.all(30), children: [
      FittedBox(
        child: Text('Settings'),
      ),
      Divider(
        thickness: 2,
      ),
      SwitchListTile(
        value: logicBloc.isDarkMode,
        onChanged: (value) => logicBloc.updateTheme(value),
        title: Text("Dark mode"),
      ),
      const SizedBox(height: 200),
      Divider(
        thickness: 2,
      ),
      ListTile(
        title: const Text('Logout'),
        onTap: () => Navigator.of(context).push(
          MaterialPageRoute(builder: (_) => const MainStateManagement()),
        ),
      )
    ]);
  }
}
