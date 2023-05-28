import 'package:flutter_test/flutter_test.dart';
import 'package:http/http.dart' as http;
import 'package:json_placeholder_app/data/repository.dart';
import 'package:json_placeholder_app/models/post.dart';
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';

// данный файл будет сгенерирован
import 'post_test.mocks.dart';

// аннотация mockito
@GenerateMocks([http.Client])
void main() {
  // создаем наш репозиторий
  final repo = Repository();
  group("fetchPosts", () {
      test('returns posts if the http call completes successfully', () async {
        // создаем фейковый клиент
        final client = MockClient();

        // ответ на запрос
        when(client.get(Uri.parse('https://jsonplaceholder.typicode.com/posts')))
            .thenAnswer((_) async => http.Response('[{"userId": 1, "id": 2, "title": "Title", "content": "Content"}]', 200));

        // проверяем корректность работы fetchPosts
        // при удачном выполнении
        final postList = await repo.fetchPosts(client: client);
        expect(postList, isA<PostList>());
        expect(postList.posts.length, 1);
        expect(postList.posts.first.title, "Title");
      });

      test('throws an exception if the http call completes with an error', () {
        final client = MockClient();

        // генерация ошибки
        when(client.get(Uri.parse('https://jsonplaceholder.typicode.com/posts')))
            .thenAnswer((_) async => http.Response('Not Found', 404));

        // проверка на исключение
        expect(repo.fetchPosts(client: client), throwsException);
      });
  });
}