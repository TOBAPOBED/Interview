import unittest
from typing import List, Any, Dict, Set

# ==========================================
# 1. БАЗОВЫЙ КЛАСС СТЭКА (С тайп-хинтами)
# ==========================================
class Stack:
    def __init__(self) -> None:
        self._items: List[Any] = []

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items.pop()

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._items[-1]

    def size(self) -> int:
        return len(self._items)


# ==========================================
# 2. КЛАСС ДЛЯ ПРОВЕРКИ СКОБОК
# ==========================================
class BracketValidator:
    def __init__(self) -> None:
        self._bracket_map: Dict[str, str] = {')': '(', ']': '[', '}': '{'}
        self._opening_brackets: Set[str] = set(self._bracket_map.values())

    def is_balanced(self, sequence: str) -> str:
        stack = Stack()
        
        for char in sequence:
            if char in self._opening_brackets:
                stack.push(char)
            elif char in self._bracket_map:
                if stack.is_empty() or stack.pop() != self._bracket_map[char]:
                    return "Несбалансированно"
                    
        return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


# ==========================================
# 3. ТЕСТЫ (Показываем знание unittest)
# ==========================================
class TestBracketValidator(unittest.TestCase):
    def setUp(self):
        self.validator = BracketValidator()

    def test_balanced_sequences(self):
        self.assertEqual(self.validator.is_balanced("(((([{}]))))"), "Сбалансированно")
        self.assertEqual(self.validator.is_balanced("[([])((([[[]]])))]{()}"), "Сбалансированно")
        self.assertEqual(self.validator.is_balanced("{{[()]}}"), "Сбалансированно")
        self.assertEqual(self.validator.is_balanced(""), "Сбалансированно") # Пустая строка тоже валидна

    def test_unbalanced_sequences(self):
        self.assertEqual(self.validator.is_balanced("}{}"), "Несбалансированно")
        self.assertEqual(self.validator.is_balanced("{{[(])]}}"), "Несбалансированно")
        self.assertEqual(self.validator.is_balanced("[[{())}]"), "Несбалансированно")
        self.assertEqual(self.validator.is_balanced("((("), "Несбалансированно") # Не закрыты

    def test_stack_methods(self):
        # На собеседовании могут попросить протестировать и сам стек!
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.size(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.size(), 1)

if __name__ == '__main__':
    unittest.main()