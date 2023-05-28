
import 'package:flutter/material.dart';

// настраиваем кастомную тему
final usualTheme = ThemeData(
  primaryColor: Colors.blueAccent,
  primaryColorLight: Colors.blueGrey[300],
  primaryColorDark: Colors.blue[300],
  primarySwatch: Colors.blueGrey,
  highlightColor: Colors.blueAccent[100],
  focusColor: Colors.blueAccent,
  // настройка Theme для AppBar
  appBarTheme: AppBarTheme(
    shadowColor: Colors.grey.withOpacity(0.8),
    elevation: 10,
  ),
  // настройка Theme для Text
  textTheme: TextTheme(
    headline5: TextStyle(fontWeight: FontWeight.bold)
  ),
  // указываем наш шрифт для всего приложения
  fontFamily: "Kalam"
);