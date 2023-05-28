
import 'package:json_placeholder_app/data/repository.dart';
import 'package:json_placeholder_app/models/photo.dart';
import 'package:mvc_pattern/mvc_pattern.dart';

// AlbumController очень поход на PostController
class AlbumController extends ControllerMVC {
  final Repository repo = Repository();

  // текущее состояние
  PhotoResult currentState = PhotoResultLoading();

  void init() async {
    try {
      // получение картинок
      final photoList = await repo.fetchPhotos();
      // успешно
      setState(() => currentState = PhotoResultSuccess(photoList));
    } catch (error) {
      // произошла ошибка
      setState(() => currentState = PhotoResultFailure("Нет интернета"));
    }
  }

}