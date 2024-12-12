import 'package:flutter/material.dart';
import 'package:widgets_app/presentation/screens/screens.dart';

class MenuItem {
  final String name;
  final String title;
  final String subtitle;
  final String link;
  final IconData icon;

  const MenuItem(
      {required this.name,
      required this.title,
      required this.subtitle,
      required this.link,
      required this.icon});
}

const appMenuItems = <MenuItem>[
  MenuItem(
    name: ButtonsScreen.name,
    title: 'Botones',
    subtitle: 'Varios botones en Flutter',
    link: '/buttons',
    icon: Icons.smart_button_outlined,
  ),
  MenuItem(
    name: CardsScreen.name,
    title: 'Tarjetas',
    subtitle: 'Un contenedor estilizado',
    link: '/cards',
    icon: Icons.credit_card,
  ),
  MenuItem(
    name: ProgressScreen.name,
    title: 'Progress',
    subtitle: 'General y controlados',
    link: '/progress',
    icon: Icons.refresh_rounded,
  ),
  MenuItem(
      name: "Snackbars",
      title: 'Snackbars y diálogos',
      subtitle: 'Indicadores de pantalla',
      link: '/snackbars',
      icon: Icons.info_outline),
  MenuItem(
      name: "Animated",
      title: "Animated contrainer",
      subtitle: "Statefull Widget Animado",
      link: "/animated",
      icon: Icons.check_box_outline_blank_rounded),
  MenuItem(
      name: "Ui",
      title: "UI Controls + Tiles",
      subtitle: "Una serie de controles en  flutter",
      link: "/ui_controls",
      icon: Icons.car_rental_outlined),
  MenuItem(
      name: "Tutorial",
      title: "Introducción a la aplicación",
      subtitle: "Pequeño tutorial introductorio",
      link: "/tutorial",
      icon: Icons.accessible_rounded)
];
