import 'package:flutter/material.dart';
import 'package:json_placeholder_app/pages/courses/education_single_page.dart';
import 'package:json_placeholder_app/pages/courses/education_video_page.dart';
import 'package:json_placeholder_app/resources/theme.dart';
import 'package:json_placeholder_app/pages/home/side_menu.dart';

// класс пони, который будет хранить имя и описание
class Pony {
  final int id;
  final String course_type;
  final String name;
  final String desc;

  Pony(this.id, this.course_type, this.name, this.desc);
}

// создаем список пони
// final указывает на то, что мы больше
final List<Pony> ponies = [
  Pony(
      0,
      "video",
      "Twillight Sparkle",
      "Twilight Sparkle is the central main character of My Little Pony Friendship is Magic. She is a female unicorn pony who transforms into an Alicorn and becomes a princess in Magical Mystery Cure"
  ),
  Pony(
      1,
      "text",
      "Starlight Glimmer",
      "Starlight Glimmer is a female unicorn pony and recurring character, initially an antagonist but later a protagonist, in the series. She first possibly appears in My Little Pony: Friends Forever Issue and first explicitly appears in the season five premiere."
  ),
  Pony(
      2,
      "text",
      "Applejack",
      "Applejack is a female Earth pony and one of the main characters of My Little Pony Friendship is Magic. She lives and works at Sweet Apple Acres with her grandmother Granny Smith, her older brother Big McIntosh, her younger sister Apple Bloom, and her dog Winona. She represents the element of honesty."
  ),
  Pony(
      3,
      "text",
      "Pinkie Pie",
      "Pinkie Pie, full name Pinkamena Diane Pie,[note 2] is a female Earth pony and one of the main characters of My Little Pony Friendship is Magic. She is an energetic and sociable baker at Sugarcube Corner, where she lives on the second floor with her toothless pet alligator Gummy, and she represents the element of laughter."
  ),
  Pony(
      4,
      "video",
      "Fluttershy",
      "https://www.youtube.com/watch?v=rd6FKVX_fJQ"
  ),
];

// TestsListPage не будет иметь состояния,
// т.к. этот пример создан только для демонстрации
// навигации в действии
class CoursesListPage extends StatelessWidget {

  // build как мы уже отметили, строит
  // иерархию наших любимых виджетов
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      drawer: SideMenu(),
      appBar: AppBar(title: Text("Pony List Page")),
      // зададим небольшие отступы для списка
      body: Padding(
        padding: EdgeInsets.symmetric(vertical: 15, horizontal: 10),
        // создаем наш список
          child: ListView(
            children: ponies.map<Widget>((pony) {
              // Material используется для того,
              // чтобы указать цвет элементу списка
              // и применить ripple эффект при нажатии на него
              return Material(
                color: usualTheme.highlightColor,
                // InkWell позволяет отслеживать
                // различные события, например: нажатие
                child: InkWell(
                  // splashColor - цвет ripple эффекта
                  splashColor: usualTheme.focusColor,
                  // нажатие на элемент списка
                  onTap: () {
                    if (pony.course_type == "text"){
                      Navigator.push(context, MaterialPageRoute(
                          builder: (context) => SingleTestPage(pony.id)
                      ));
                    } else {
                      Navigator.push(context, MaterialPageRoute(
                          builder: (context) => SingleVideoPage(pony.id)
                      ));
                    }
                  },
                  // далее указываем в качестве
                  // элемента Container с вложенным Text
                  // Container позволяет указать внутренние (padding)
                  // и внешние отступы (margin),
                  // а также тень, закругление углов,
                  // цвет и размеры вложенного виджета
                  child: Container(
                      padding: EdgeInsets.all(15),
                      child: Text(
                          pony.name,
                          style: Theme.of(context).textTheme.headline4!.copyWith(color: Colors.white)
                      )
                  ),
                ),
              );
              // map возвращает Iterable объект, который необходимо
              // преобразовать в список с помощью toList() функции
            }).toList(),
          )
      ),
    );
  }

}