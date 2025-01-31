import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:state_management/state_managemente/no_package/home_bloc.dart';
import 'package:state_management/state_managemente/package/menu_page.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Home'),
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
                    child: Consumer<HomeBloc>(
                      builder: (context, bloc, _) => Row(
                        children: [
                          Expanded(
                              child: InkWell(
                            onTap: bloc.incrementCounter,
                            child: FittedBox(
                              child: Text('+'),
                            ),
                          )),
                          Expanded(
                              child: InkWell(
                            onTap: bloc.decrementCounter,
                            child: FittedBox(
                              child: Text('-'),
                            ),
                          ))
                        ],
                      ),
                    ))),
          ],
        ),
      ),
      bottomNavigationBar: SizedBox(
        height: 100,
        child: TotalWidget(),
      ),
    );
  }
}

class TotalWidget extends StatelessWidget {
  const TotalWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: Colors.blue,
      height: 100,
      child: Padding(
          padding: const EdgeInsets.all(20),
          child: FittedBox(
            child: Consumer<HomeBloc>(
              builder: (context, bloc, _) => Text(
                '${bloc.counter}',
                style: const TextStyle(fontSize: 30),
              ),
            ),
          )),
    );
  }
}
