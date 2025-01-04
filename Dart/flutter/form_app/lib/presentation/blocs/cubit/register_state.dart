part of 'register_cubit.dart';

enum FormStatus { invalid, valid, validating, posting }

class RegisterState extends Equatable {
  final FormStatus formStatus;
  final String username;
  final String email;
  final String password;
  const RegisterState({
    this.formStatus = FormStatus.invalid,
    this.username = '',
    this.email = '',
    this.password = '',
  });

  RegisterState copyWith({
    FormStatus? formStatus,
    String? username,
    String? email,
    String? password,
  }) {
    return RegisterState(
      formStatus: formStatus ?? this.formStatus,
      username: username ?? this.username,
      email: email ?? this.email,
      password: password ?? this.password,
    );
  }

  @override
  List<Object> get props => [formStatus, username, email, password];
}
