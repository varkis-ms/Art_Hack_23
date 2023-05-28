
import 'package:flutter/material.dart';

// будет хранить основную информацию
// об элементах меню
class MyTab {
  final String? name;
  final MaterialColor? color;
  final IconData? icon;

  const MyTab({this.name, this.color, this.icon});
}

// пригодиться для определения
// выбранного элемента меню
enum TabItem { NEWS, COURSES, TESTS, MAPS}