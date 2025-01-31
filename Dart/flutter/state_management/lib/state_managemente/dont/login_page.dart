import 'package:flutter/material.dart';
import 'package:state_management/state_managemente/dont/home_page.dart';

bool isDarkMode = false;

class LoginMainPage extends StatefulWidget {
  const LoginMainPage({super.key});

  @override
  State<LoginMainPage> createState() => _LoginMainPageState();
}

class _LoginMainPageState extends State<LoginMainPage> {
  void onThemeUpdated(bool darkMode) {
    setState(() {
      isDarkMode = darkMode;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: isDarkMode ? ThemeData.dark() : ThemeData.light(),
      home: LoginPage(
        onThemeSelected: onThemeUpdated,
      ),
    );
  }
}

class LoginPage extends StatelessWidget {
  final ValueChanged<bool> onThemeSelected;

  const LoginPage({
    super.key,
    required this.onThemeSelected,
  });

  void _onTab(BuildContext context) {
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (_) => HomePage(
          onThemeSelected: onThemeSelected,
        ),
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
