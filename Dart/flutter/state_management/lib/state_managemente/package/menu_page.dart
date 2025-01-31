import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:state_management/state_managemente/main_state_management.dart';
import 'package:state_management/state_managemente/no_package/login_bloc.dart';

class MenuPage extends StatelessWidget {
  const MenuPage({super.key});

  @override
  Widget build(BuildContext context) {
    final loginBloc = Provider.of<LoginBloc>(context);

    return ListView(padding: const EdgeInsets.all(30), children: [
      FittedBox(
        child: Text('Settings'),
      ),
      Divider(
        thickness: 2,
      ),
      SwitchListTile(
        value: loginBloc.isDarkMode,
        onChanged: (value) => loginBloc.updateTheme(value),
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
