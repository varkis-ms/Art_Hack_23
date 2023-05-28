
import 'package:flutter/material.dart';
import 'package:json_placeholder_app/resources/theme.dart';

import 'education_list_page.dart';

// также, как и TestsListPage наша страница
// не будет иметь состояния
class SingleTestPage extends StatelessWidget {
  final int testId;

  SingleTestPage(this.testId);

  @override
  Widget build(BuildContext context) {
    final pony = ponies[testId];
    return Scaffold(
      appBar: AppBar(
        title: Text("Pony Detail Page"),
      ),
      body: Padding(
        // указываем отступ для контента
        padding: EdgeInsets.all(15),
        // Column размещает дочерние виджеты в виде колонки
        // crossAxisAlignment - выравнивание по ширине (колонка) или
        // по высоте (строка)
        // mainAxisAlignment работает наоборот
        // в данном случае мы растягиваем дочерние элементы
        // на всю ширину колонки
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Container(
                padding: EdgeInsets.all(10),
                // вы не можете указать color для Container,
                // т.к. свойство decoration было определено
                // color: Colors.pinkAccent,

                // BoxDecoration имеет дополнительные свойства,
                // посравнению с Container,
                // такие как gradient, borderRadius, border, shape
                // и boxShadow
                // здесь мы задаем радиус закругления левого и правого
                // верхних углов
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.only(
                      topLeft: Radius.circular(15),
                      topRight: Radius.circular(15)
                  ),
                  // обратите внимание,
                  // если вы указываете параметр decoration,
                  // то вы не можете указать цвет для Container
                  color: usualTheme.highlightColor,
                ),
                child: Text(
                    // указываем имя pony
                    pony.name,
                    style: Theme.of(context).textTheme.headline4!.copyWith(color: Colors.white),
                )
            ),
            Container(
                padding: EdgeInsets.all(10),
                child: Text(
                    // указываем описание pony
                    pony.desc,
                    style: Theme.of(context).textTheme.bodyText1
                )
            )
          ],
        ),
      )
    );
  }
}