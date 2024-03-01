# Реализовать АТД стека, включающий, помимо базовых, следующие операции: 1) empty() - проверка на пустоту 2) top() –
# возвращает верхний элемент, не удаляя его из стека 3) next_to_top() – возвращает второй сверху элемент,
# не удаляя его из стека 4) error() – сообщение об ошибке, когда происходит добавление в полностью заполненный стек
# или удаление из пустого стека 5) dump() – вывод содержимого стека на экран 6) clear() – очистить стек(но не
# удалить) 7) count() – подсчёт количества элементов на базе 1) массива (для чётных вариантов) 2) связного списка(для
# нечётных вариантов)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def error():
    print("Ошибка: Стек пустой")


class LinkedListStack:
    def __init__(self):
        self.top_node = None
        self.size = 0

    def empty(self):
        return self.size == 0

    def top(self):
        if not self.empty():
            return self.top_node.data
        else:
            error()

    def next_to_top(self):
        if self.size >= 2:
            current = self.top_node
            for _ in range(self.size - 2):
                current = current.next
            return current.data
        else:
            error()

    def dump(self):
        current = self.top_node
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def clear(self):
        self.top_node = None
        self.size = 0

    def count(self):
        return self.size

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top_node
        self.top_node = new_node
        self.size += 1

    def pop(self):
        if not self.empty():
            self.top_node = self.top_node.next
            self.size -= 1
        else:
            error()


# Пример использования стека на основе связного списка:
stack = LinkedListStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.dump()  # Вывод содержимого стека: 3 -> 2 -> 1 -> None
print("Верхний элемент:", stack.top())  # Верхний элемент: 3
print("Второй сверху элемент:", stack.next_to_top())  # Второй сверху элемент: 2
stack.pop()
stack.dump()  # Вывод содержимого стека после pop(): 2 -> 1 -> None
print("Количество элементов:", stack.count())  # Количество элементов: 2
stack.clear()
stack.dump()  # Вывод содержимого стека после clear(): None
