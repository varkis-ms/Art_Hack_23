// class UserInfo(BaseModel):

// score: int | None = None
// birthday: date | None = None changlable
// displayed_name: str | None = None changable
// full_name: str | None = None
//


import 'dart:convert';

class User {
  // все поля являются private
  // это сделано для инкапсуляции данных
  final String? _login;
  final String? _email;
  final int? _score;
  final String? _birthday;
  final String? _displayed_name;
  final String? _full_name;

  // создаем getters для наших полей
  // дабы только мы могли читать их
  String? get login => _login;
  String? get email => _email;
  int? get score => _score;
  String? get birthday => _birthday;
  String? get displayed_name => _displayed_name;
  String? get full_name => _full_name;


  // добавим новый конструктор для поста
  User(this._login, this._email, this._score, this._birthday, this._displayed_name, this._full_name);

  String toJson() {
    return json.encode({
      "login": _login,
      "email": _email,
      "score": _score,
      "birthday": _birthday,
      "displayed_name": _displayed_name,
      "full_name": _full_name
    });
  }

  // Dart позволяет создавать конструкторы с разными именами
  // User.fromJson(json) - это конструктор
  // здесь мы принимаем объект поста и получаем его поля
  // обратите внимание, что dynamic переменная
  // может иметь разные типы: String, int, double и т.д.
  User.fromJson(Map<String, dynamic> json) :
        this._login = json["login"],
        this._email = json["email"],
        this._score = json["score"],
        this._birthday = json["birthday"],
        this._displayed_name = json["displayed_name"],
        this._full_name = json["full_name"];
}

class UserList {
  final List<User> users = [];
  UserList.fromJson(List<dynamic> jsonItems) {
    for (var jsonItem in jsonItems) {
      users.add(User.fromJson(jsonItem));
    }
  }
}

// у нас будут только два состояния
abstract class UserEdit {}

// успешное добавление
class UserEditSuccess extends UserEdit {}
// ошибка
class UserEditFailure extends UserEdit {}

// наше представление будет получать объекты
// этого класса и определять конкретный его
// подтип
abstract class UserResult {}

// указывает на успешный запрос
class UserResultSuccess extends UserResult {
  final UserList userList;
  UserResultSuccess(this.userList);
}

// произошла ошибка
class UserResultFailure extends UserResult {
  final String error;
  UserResultFailure(this.error);
}

// загрузка данных
class UserResultLoading extends UserResult {
  UserResultLoading();
}