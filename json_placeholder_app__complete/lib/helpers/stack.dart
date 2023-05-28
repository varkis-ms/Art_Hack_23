
class Stack<T> {
  final stack = <T>[];

  void push(T t) {
    stack.add(t);
  }

  T? pop() {
    if (isEmpty) {
      return null;
    }
    return stack.removeLast();
  }

  bool get isEmpty => stack.isEmpty;
}