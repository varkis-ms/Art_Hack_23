import 'package:flutter/material.dart';
import 'package:mvc_pattern/mvc_pattern.dart';
import '../models/tab.dart';

// библиотека mvc_pattern предлагает
// нам специальный класс ControllerMVC,
// который предоставит нам setState метод
class HomeController extends ControllerMVC {

  // ссылка на объект самого контроллера
  static HomeController? _this;
  static HomeController? get controller => _this;

  // сам по себе factory конструктор не создает
  // экземляра класса HomeController
  // и используется для различных кастомных вещей
  // в данном случае мы реализуем паттерн Singleton
  // то есть будет существовать единственный экземпляр
  // класса HomeController
  factory HomeController() {
    if (_this == null) _this = HomeController._();
    return _this!;
  }

  HomeController._();

  // GlobalKey будет хранить уникальный ключ,
  // по которому мы сможем получить доступ
  // к виджетам, которые уже находяться в иерархии
  // NavigatorState - состояние Navigator виджета
  // знак _ как уже было отмечено указывает на то,
  // что это private переменная, поэтому мы
  // не сможем получить доступ извне к _navigatorKeys
  final _navigatorKeys = {
    TabItem.NEWS: GlobalKey<NavigatorState>(),
    TabItem.COURSES: GlobalKey<NavigatorState>(),
    TabItem.TESTS: GlobalKey<NavigatorState>(),
    TabItem.MAPS: GlobalKey<NavigatorState>(),
  };

  // ключевое слово get указывает на getter
  // мы сможем только получить значение  _navigatorKeys,
  // но не сможем его изменить
  // это называеться инкапсуляцией данных (один из принципов ООП)
  Map<TabItem, GlobalKey> get navigatorKeys => _navigatorKeys;

  // текущий выбранный элемент
  var _currentTab = TabItem.NEWS;

  // то же самое и для текущего выбранного пункта меню
  TabItem get currentTab => _currentTab;

  // выбор элемента меню
  // здесь мы делаем функцию selectTab публичной
  // чтобы смогли получить доступ из HomePage
  // обратите внимание, что библиотека mvc_pattern
  // предоставляет нам возможность иметь состояние в контроллере,
  // что очень удобно
  void selectTab(TabItem tabItem) {
    setState(() => _currentTab = tabItem);
  }


}