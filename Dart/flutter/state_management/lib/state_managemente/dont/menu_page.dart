import 'package:flutter/material.dart';
import 'package:state_management/state_managemente/dont/login_page.dart';
import 'package:state_management/state_managemente/main_state_management.dart';

class MenuPage extends StatelessWidget {
  final ValueChanged<bool> onThemeSelected;
  const MenuPage({super.key, required this.onThemeSelected});

  @override
  Widget build(BuildContext context) {
    return ListView(padding: const EdgeInsets.all(30), children: [
      FittedBox(
        child: Text('Settings'),
      ),
      Divider(
        thickness: 2,
      ),
      SwitchListTile(
        value: isDarkMode,
        onChanged: (value) => onThemeSelected(value),
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
