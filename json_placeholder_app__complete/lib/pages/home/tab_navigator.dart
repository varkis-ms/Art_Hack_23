
import 'package:flutter/material.dart';
import 'package:json_placeholder_app/pages/courses/education_list_page.dart';
import 'package:json_placeholder_app/pages/post/post_list_page.dart';
import 'package:json_placeholder_app/pages/tests/test_list_page.dart';
import '../../models/tab.dart';


class TabNavigator extends StatelessWidget {
  // TabNavigator принимает:
  // navigatorKey - уникальный ключ для NavigatorState
  // tabItem - текущий пункт меню
  TabNavigator({this.navigatorKey, this.tabItem});

  final GlobalKey<NavigatorState>? navigatorKey;
  final TabItem? tabItem;

  @override
  Widget build(BuildContext context) {
    // наконец-то мы дошли до этого момента
    // здесь мы присваиваем navigatorKey
    // только, что созданному Navigator'у
    // navigatorKey, как уже было отмечено является ключом,
    // по которому мы получаем доступ к состоянию
    // Navigator'a, вот и все!
    return Navigator(
      key: navigatorKey,
      // Navigator имеет параметр initialRoute,
      // который указывает начальную страницу и является
      // всего лишь строкой.
      // Мы не будем вдаваться в подробности, но отметим,
      // что по умолчанию initialRoute равен /
      // initialRoute: "/",

      onGenerateRoute: (routeSettings) {
        // сначала определяем текущую страницу
        Widget currentPage;
        if (tabItem == TabItem.COURSES) {
          // пока мы будем использовать PonyListPage
          currentPage = CoursesListPage();
        } else if (tabItem == TabItem.NEWS) {
          currentPage = PostListPage();
        } else {
          currentPage = TestsListPage();
        }
        // строим Route (страница или экран)
        return MaterialPageRoute(builder: (context) => currentPage);
      },
    );
  }

}