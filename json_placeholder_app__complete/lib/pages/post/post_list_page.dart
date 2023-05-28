
import 'package:flutter/material.dart';
import '../../controllers/post_controller.dart';
import '../../models/post.dart';
import 'post_list_item.dart';
import 'package:mvc_pattern/mvc_pattern.dart';
import 'package:json_placeholder_app/pages/home/side_menu.dart';


class PostListPage extends StatefulWidget {
  @override
  _PostListPageState createState() => _PostListPageState();
}

// не забываем расширяться от StateMVC
class _PostListPageState extends StateMVC {

  // ссылка на наш контроллер
  late PostController _controller;

  // передаем наш контроллер StateMVC конструктору и
  // получаем на него ссылку
  _PostListPageState() : super(PostController()) {
    _controller = controller as PostController;
  }

  // после инициализации состояние
  // мы запрашивает данные у сервера
  @override
  void initState() {
    super.initState();
    _controller.init();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Новостная лента"),
      ),
      body: _buildContent(),

    );
  }

  Widget _buildContent() {
    // первым делом получаем текущее состояние
    final state = _controller.currentState;
    if (state is PostResultLoading) {
      // загрузка
      return Center(
        child: CircularProgressIndicator(),
      );
    } else if (state is PostResultFailure) {
      // ошибка
      return Center(
        child: Text(
          state.error,
          textAlign: TextAlign.center,
          style: Theme.of(context).textTheme.headline4!.copyWith(color: Colors.red)
        ),
      );
    } else {
      // отображаем список постов
      final posts = (state as PostResultSuccess).postList.posts;
      return Padding(
        padding: EdgeInsets.all(10),
        // ListView.builder создает элемент списка
        // только когда он видим на экране
        child: ListView.builder(
          itemCount: posts.length,
          itemBuilder: (context, index) {
            // мы вынесли элемент списка в
            // отдельный виджет
            return PostListItem(posts[index]);
          },
        ),
      );
    }
  }


}



