import 'package:flutter/material.dart';
import 'package:state_management/state_managemente/no_package/home_page.dart';
import 'package:state_management/state_managemente/no_package/login_bloc.dart';

class LoginMainPage extends StatefulWidget {
  const LoginMainPage({super.key});

  @override
  State<LoginMainPage> createState() => _LoginMainPageState();
}

class _LoginMainPageState extends State<LoginMainPage> {
  final LoginBloc loginBloc = LoginBloc();

  @override
  Widget build(BuildContext context) {
    return MyIngeretedWidget(
        loginBloc: loginBloc,
        child: AnimatedBuilder(
            animation: loginBloc,
            builder: (context, _) {
              return MaterialApp(
                debugShowCheckedModeBanner: false,
                theme:
                    loginBloc.isDarkMode ? ThemeData.dark() : ThemeData.light(),
                home: LoginPage(),
              );
            }));
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

class MyIngeretedWidget extends InheritedWidget {
  final LoginBloc loginBloc;

  const MyIngeretedWidget({
    super.key,
    required super.child,
    required this.loginBloc,
  });

  static MyIngeretedWidget? of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType();

  @override
  bool updateShouldNotify(MyIngeretedWidget oldWidget) => true;
}
