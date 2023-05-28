
class Photo {
  final int _id;
  final String _title;
  final String _url;

  String get url => _url;

  Photo.fromJson(Map<String, dynamic> json) :
      _id = json["id"],
      _title = json["title"],
      _url = json["url"];
}

class PhotoList {
  final List<Photo> photos = [];

  PhotoList.fromJson(List<dynamic> jsonItems) {
    for (var jsonItem in jsonItems) {
      photos.add(Photo.fromJson(jsonItem));
    }
  }

}

abstract class PhotoResult {}

class PhotoResultSuccess extends PhotoResult {
  final PhotoList photoList;
  PhotoResultSuccess(this.photoList);
}

// произошла ошибка
class PhotoResultFailure extends PhotoResult {
  final String error;
  PhotoResultFailure(this.error);
}

// загрузка данных
class PhotoResultLoading extends PhotoResult {
  PhotoResultLoading();
}