import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:state_management/state_managemente/no_package/home_bloc.dart';
import 'package:state_management/state_managemente/no_package/login_bloc.dart';
import 'package:state_management/state_managemente/package/home_page.dart';

class LoginMainPage extends StatelessWidget {
  const LoginMainPage({super.key});
  @override
  Widget build(BuildContext context) {
    return MultiProvider(
        providers: [
          ChangeNotifierProvider(create: (_) => LoginBloc()),
          ChangeNotifierProvider(create: (_) => HomeBloc()),
        ],
        child: Consumer<LoginBloc>(
          builder: (context, bloc, _) => MaterialApp(
            debugShowCheckedModeBanner: false,
            theme: bloc.isDarkMode ? ThemeData.dark() : ThemeData.light(),
            home: LoginPage(),
          ),
        ));
  }
}

class LoginPage extends StatelessWidget {
  const LoginPage({
    super.key,
  });

  void _onTab(BuildContext context) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (_) => HomePage(),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
      ),
      body: Padding(
          padding: const EdgeInsets.all(8),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                decoration: InputDecoration(
                  hintText: "Username",
                ),
              ),
              const SizedBox(height: 30),
              TextField(
                obscureText: true,
                decoration: InputDecoration(
                  hintText: "Password",
                ),
              ),
              const SizedBox(height: 30),
              FilledButton(
                onPressed: () {
                  _onTab(context);
                },
                child: const Text('Login'),
              ),
            ],
          )),
    );
  }
}
