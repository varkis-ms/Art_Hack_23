
import 'package:flutter_test/flutter_test.dart';
import 'package:json_placeholder_app/helpers/stack.dart';

void main() {
  group("Stack", () {
    test("Stack should be empty", () {
      expect(Stack().isEmpty, true);
    });
    test("Stack shouldn't be empty", () {
      final stack = Stack<int>();
      stack.push(5);
      expect(stack.isEmpty, false);
    });
    test("Stack should be popped", () {
      final stack = Stack<int>();
      stack.push(5);
      expect(stack.pop(), 5);
    });
    test("Stack should be work correctly", () {
      final stack = Stack<int>();
      stack.push(1);
      stack.push(2);
      stack.push(5);
      expect(stack.pop(), 5);
      expect(stack.pop(), 2);
      expect(stack.isEmpty, false);
    });
  });
}