class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def swap_nodes(self, data1, data2):
        if data1 == data2:
            return

        node1 = None
        node2 = None
        current = self.head

        while current:
            if current.data == data1:
                node1 = current
            elif current.data == data2:
                node2 = current

            current = current.next

        if not node1 or not node2:
            return  # Один из узлов не найден, ничего не меняем

        # Обновляем указатели предыдущего и следующего узлов для соседних узлов
        if node1.prev:
            node1.prev.next = node2
        else:
            self.head = node2

        if node2.prev:
            node2.prev.next = node1
        else:
            self.head = node1

        if node1.next:
            node1.next.prev = node2

        if node2.next:
            node2.next.prev = node1

        # Меняем указатели на предыдущий и следующий узлы для обоих узлов
        temp_prev = node1.prev
        node1.prev = node2.prev
        node2.prev = temp_prev

        temp_next = node1.next
        node1.next = node2.next
        node2.next = temp_next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Пример использования
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.append(7)

    print("Исходный список:")
    dll.display()

    dll.swap_nodes(2, 3)

    print("Список после обмена узлов 1 и 2:")
    dll.display()
