
import 'package:flutter/material.dart';
import 'package:flutter_staggered_grid_view/flutter_staggered_grid_view.dart';
import 'package:json_placeholder_app/controllers/album_controller.dart';
import 'package:json_placeholder_app/models/photo.dart';
import 'package:json_placeholder_app/pages/home/side_menu.dart';
import 'package:mvc_pattern/mvc_pattern.dart';
import 'package:json_placeholder_app/pages/home/side_menu.dart';

class AlbumListPage extends StatefulWidget {
  @override
  _AlbumListPageState createState() => _AlbumListPageState();
}

class _AlbumListPageState extends StateMVC {

  // добавляем наш контроллер
  // late указывает на отложенную инициализацию
  late AlbumController _controller;

  _AlbumListPageState() : super(AlbumController()){
    _controller = controller as AlbumController;
  }

  @override
  void initState() {
    super.initState();
    // получаем картинки из JSONPlaceholder
    _controller.init();
  }


  @override
  Widget build(BuildContext context) {
    return Scaffold(
        drawer: SideMenu(),
        appBar: AppBar(
          title: Text("Album List Page"),
        ),
        body: _buildContent()
    );
  }

  Widget _buildContent() {
    // получение текущего состояния
    final state = _controller.currentState;
    if (state is PhotoResultLoading) {
      // загрузка
      return Center(
        child: CircularProgressIndicator(),
      );
    } else if (state is PhotoResultFailure) {
      // ошибка
      return Center(
        child: Text(
            state.error,
            textAlign: TextAlign.center,
            style: Theme.of(context).textTheme.headline4!.copyWith(color: Colors.red)
        ),
      );
    } else {
      final images = (state as PhotoResultSuccess).photoList.photos;
      // мы используем StaggeredGridView для построения
      // кастомной сетки из изображений
      return StaggeredGridView.countBuilder(
        // количество изображений
        itemCount: images.length,
        // crossAxisCount задает количество колонок
        // по которым будут выравнены изображения
        crossAxisCount: 8,
        // отступы по вертикали
        mainAxisSpacing: 10,
        // отступы по горизонтали
        crossAxisSpacing: 10,
        staggeredTileBuilder: (index) {
          // каждое изображение будет в ширину 4 колонки (первый параметр)
          // изображения на четных индексах будут в 2 раза меньше (второй параметр)
          return StaggeredTile.count(4, index % 2 == 0 ? 4 : 8);
        },
        // строим изображение
        itemBuilder: (context, index) {
          return Container(
            decoration: BoxDecoration(
                border: Border.all(color: Colors.pinkAccent, width: 1)
            ),
            // мы испольуем метод network для
            // отображения картинки из сети
            child:  Image.network(
              images[index].url,
              // указываем максимальную ширину и высоту
              width: double.infinity,
              height: double.infinity,
              // указываем масштабирование изображения
              fit: BoxFit.cover,
              // при загрузки изображения
              // будет показан текст Loading...
              loadingBuilder: (context, widget, imageChunkEvent) {
                if (imageChunkEvent == null) {
                  return widget;
                }
                return Center(child: Text("Loading..."));
              },
              // при возникновении ошибки
              // вместо изображения будет текст Error!
              errorBuilder: (context, obj, stacktrace) => Center(child: Text("Error!")),
            ),
          );
        },

      );
    }
  }
}