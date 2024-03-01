class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_nodes_at_odd_positions(head):
    if not head or not head.next:
        # Список пуст или содержит только один узел, ничего удалять не нужно
        return

    current = head
    while current and current.next:
        temp = current.next
        current.next = temp.next
        temp = None
        current = current.next


def display_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Создаем пример связного списка
head = Node(1)
current = head
for i in range(2, 11):
    current.next = Node(i)
    current = current.next

print("Исходный список:")
display_list(head)

# Удаляем узлы в нечетных позициях
delete_nodes_at_odd_positions(head)

print("Список после удаления узлов в нечетных позициях:")
display_list(head)
