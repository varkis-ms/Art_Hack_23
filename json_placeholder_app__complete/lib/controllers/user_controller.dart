
import 'dart:async';

import '../data/repository.dart';
import '../models/user.dart';
import 'package:mvc_pattern/mvc_pattern.dart';

class UserController extends ControllerMVC {
  // создаем наш репозиторий
  final Repository repo = new Repository();

  // конструктор нашего контроллера
  UserController();

  // первоначальное состояние - загрузка данных
  UserResult currentState = UserResultLoading();

  void init() async {
    try {
      // получаем данные из репозитория
      final UserList = await repo.fetchUsers();
      // если все ок то обновляем состояние на успешное
      setState(() => currentState = UserResultSuccess(UserList));
    } catch (error) {
      // в противном случае произошла ошибка
      setState(() => currentState = UserResultFailure("Нет интернета"));
    }
  }

  // добавление поста
  // функция addUser будет принимать callback,
  // через который мы будет получать ответ
  void editUser(User User, void Function(UserEdit) callback) async {
    try {
      final result = await repo.editUser(User);
      // сервер вернул результат
      callback(result);
    } catch (error) {
      // произошла ошибка
      callback(UserEditFailure());
    }
  }

  Future<User> getUser(int id) async {
    try {
      final result = await repo.getUser(id);
      // сервер вернул результат
      return result;
    } catch (error) {
      // произошла ошибка
      throw("error");
    }
  }


}

