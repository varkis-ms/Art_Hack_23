
import 'package:flutter/material.dart';
import 'package:json_placeholder_app/controllers/user_controller.dart';
import 'package:json_placeholder_app/models/user.dart';
import 'package:mvc_pattern/mvc_pattern.dart';

class EditPersonalDataPage extends StatefulWidget {

  @override
  _EditPersonalDataPageState createState() => _EditPersonalDataPageState();
}

// не забываем расширять StateMVC
class _EditPersonalDataPageState extends StateMVC {

  // _controller может быть null
  UserController? _controller;

  // получаем UserController
  _EditPersonalDataPageState() : super(UserController()) {
    _controller = controller as UserController;
  }

  // TextEditingController'ы позволят нам получить текст из полей формы
  final TextEditingController birthdayController = TextEditingController();
  final TextEditingController displayNameController = TextEditingController();
  final TextEditingController emailController = TextEditingController();

  // _formState пригодится нам для валидации
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    // todo: get here
    // todo: this https://pub.dev/packages/shared_preferences to global user fields

    return Scaffold(
      appBar: AppBar(
        title: Text("User Edit Page"),
        actions: [
          // пункт меню в AppBar
          IconButton(
            icon: Icon(Icons.check),
            onPressed: () {
              // сначала запускаем валидацию формы
              if (_formKey.currentState!.validate()) {
                // создаем пост
                // получаем текст через TextEditingController
                final user = User(
                  "my.ogin", emailController.text, 5, birthdayController.text,
                  displayNameController.text, "asdfjashdfjkdhaskjf"
                );

                _controller!.editUser(user, (status) {

                    Navigator.pop(context, "very good");

                });
              }
            },
          )
        ],
      ),
      body: Padding(
        padding: EdgeInsets.all(15),
        child: _buildContent(User("123", "456", 5, "678", "13", "1234")),
      ),
    );
  }

  Widget _buildContent(User oldUser) {
    // построение формы
    return Form(
      key: _formKey,
      // у нас будет два поля
      child: Column(
        children: [
          // поля для ввода заголовка
          TextFormField(
            // указываем для поля границу,
            // иконку и подсказку (hint)
            decoration: InputDecoration(
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.face),
                hintText: "Заголовок"
            ),
            // указываем контроллер
            controller: birthdayController,
            // параметр validator - функция которая,
            // должна возвращать null при успешной проверки
            // и строку при неудачной
            validator: (value) {
              // здесь мы для наглядности добавили 2 проверки
              if (value == null || value.isEmpty) {
                return "Заголовок пустой";
              }
              if (value.length < 3) {
                return "Заголовок должен быть не короче 3 символов";
              }
              return null;
            },
          ),
          TextFormField(
            // указываем для поля границу,
            // иконку и подсказку (hint)
            decoration: InputDecoration(
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.face),
                hintText: "Заголовок"
            ),
            // указываем контроллер
            controller: emailController,
            validator: (value) {
              // здесь мы для наглядности добавили 2 проверки
              if (value == null || value.isEmpty) {
                return "Заголовок пустой";
              }
              if (!value.contains('@')) {
                return "Почта должен содержать знак @";
              }
              return null;
            },
          ),
          TextFormField(
            // указываем для поля границу,
            // иконку и подсказку (hint)
            decoration: InputDecoration(
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.face),
                hintText: "ИМЯ"
            ),
            // указываем контроллер
            controller: displayNameController,
            validator: (value) {
              // здесь мы для наглядности добавили 2 проверки
              if (value == null || value.isEmpty) {
                return "Заголовок пустой";
              }
              if (!value.contains('@')) {
                return "Почта должен содержать знак @";
              }
              return null;
            },
          ),
          TextFormField(
            readOnly: true,
    initialValue: oldUser.login,
            // указываем для поля границу,
            // иконку и подсказку (hint)
            decoration: InputDecoration(
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.face),
                hintText: "login"
            ),
          ),
          // небольшой отступ между полями
          SizedBox(height: 10),
          // Expanded означает, что мы должны
          // расширить наше поле на все доступное пространство
          Expanded(
            child: TextFormField(
              // maxLines: null и expands: true
              // указаны только для расширения поля на всю
              // доступную высоту
              maxLines: null,
              expands: true,
              textAlignVertical: TextAlignVertical.top,
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: "Содержание",
              ),
              // указываем контроллер
              controller: displayNameController,
              // также добавляем проверку поля
              validator: (value) {
                if (value == null || value.isEmpty) {
                  return "Содержание пустое";
                }
                return null;
              },
            ),
          )
        ],
      ),
    );
  }

}