import 'package:flutter/material.dart';
import 'package:state_management/state_managemente/no_package/home_bloc.dart';
import 'package:state_management/state_managemente/no_package/menu_page.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final HomeBloc homeBloc = HomeBloc();

  @override
  Widget build(BuildContext context) {
    return HomeInheritedWidget(
      homeBloc: homeBloc,
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Home No Package'),
        ),
        drawer: Drawer(
          child: MenuPage(),
        ),
        body: Center(
          child: Column(
            children: [
              Expanded(
                  child: Padding(
                      padding: const EdgeInsets.all(20),
                      child: Row(
                        children: [
                          Expanded(
                              child: InkWell(
                            onTap: homeBloc.incrementCounter,
                            child: FittedBox(
                              child: Text('+'),
                            ),
                          )),
                          Expanded(
                              child: InkWell(
                            onTap: homeBloc.decrementCounter,
                            child: FittedBox(
                              child: Text('-'),
                            ),
                          ))
                        ],
                      ))),
            ],
          ),
        ),
        bottomNavigationBar: SizedBox(
          height: 100,
          child: TotalWidget(),
        ),
      ),
    );
  }
}

class HomeInheritedWidget extends InheritedWidget {
  final HomeBloc homeBloc;

  const HomeInheritedWidget({
    super.key,
    required super.child,
    required this.homeBloc,
  });

  static HomeInheritedWidget? of(BuildContext context) =>
      context.dependOnInheritedWidgetOfExactType();

  @override
  bool updateShouldNotify(HomeInheritedWidget oldWidget) => true;
}

class TotalWidget extends StatelessWidget {
  const TotalWidget({super.key});

  @override
  Widget build(BuildContext context) {
    final HomeBloc homeBloc = HomeInheritedWidget.of(context)!.homeBloc;
    return Container(
      color: Colors.blue,
      height: 100,
      child: Padding(
          padding: const EdgeInsets.all(20),
          child: AnimatedBuilder(
            animation: homeBloc,
            builder: (context, child) {
              return Center(
                child: Text(
                  '${homeBloc.counter}',
                  style: const TextStyle(fontSize: 30),
                ),
              );
            },
          )),
    );
  }
}
