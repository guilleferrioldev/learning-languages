import 'package:flutter/material.dart';
import 'package:form_app/presentation/widgets/widgets.dart';

class RegisterScreen extends StatelessWidget {
  const RegisterScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Register'),
      ),
      body: const _RegisterView(),
    );
  }
}

class _RegisterView extends StatelessWidget {
  const _RegisterView();

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 10),
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              const FlutterLogo(size: 100),
              const SizedBox(height: 30),
              const _RegisterFom(),
              const SizedBox(height: 30),
            ],
          ),
        ),
      ),
    );
  }
}

class _RegisterFom extends StatefulWidget {
  const _RegisterFom();

  @override
  State<_RegisterFom> createState() => _RegisterFomState();
}

class _RegisterFomState extends State<_RegisterFom> {
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();
  String username = '';
  String email = '';
  String password = '';

  @override
  Widget build(BuildContext context) {
    return Form(
        key: _formKey,
        child: Column(
          children: [
            CustomTextFormField(
              labelText: 'Username',
              onChanged: (value) => username = value,
              validator: (value) {
                if (value!.isEmpty | value.trim().isEmpty) {
                  return 'Username required';
                }

                if (value.length < 6) {
                  return 'Username must be at least 6 characters';
                }

                return null;
              },
            ),
            const SizedBox(height: 20),
            CustomTextFormField(
              labelText: 'Email',
              onChanged: (value) => email = value,
              validator: (value) {
                if (value!.isEmpty | value.trim().isEmpty) {
                  return 'Email required';
                }

                final emailRegExp = RegExp(
                  r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$',
                );

                if (!emailRegExp.hasMatch(value)) {
                  return 'Invalid email address';
                }

                return null;
              },
            ),
            const SizedBox(height: 20),
            CustomTextFormField(
              labelText: 'Password',
              onChanged: (value) => password = value,
              obscureText: true,
              validator: (value) {
                if (value!.isEmpty | value.trim().isEmpty) {
                  return 'Password required';
                }

                if (value.length < 6) {
                  return 'Password must be at least 6 characters';
                }

                return null;
              },
            ),
            const SizedBox(height: 20),
            FilledButton.tonalIcon(
                onPressed: () {
                  bool isValid = _formKey.currentState!.validate();
                  if (isValid) {
                    print('$username $email $password');
                  } else {
                    print('Form is not valid');
                  }
                },
                icon: Icon(Icons.save),
                label: Text('Create user')),
          ],
        ));
  }
}
