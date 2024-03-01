class IndexLinkedList:
    def __init__(self, data):
        self.data = data
        self.next_index = None


def copy_list_with_indices(input_list):
    if not input_list:
        return None

    # Создаем массив индексов
    indices = list(range(len(input_list)))

    # Создаем связный список с индексами
    head = IndexLinkedList(input_list[indices[0]])
    current = head

    for i in indices[1:]:
        current.next_index = IndexLinkedList(input_list[i])
        current = current.next_index

    return head


# Функция для печати связного списка
def print_linked_list(linked_list):
    current = linked_list
    while current:
        print(current.data, end=" -> ")
        current = current.next_index
    print("None")


# Пример использования:
original_list = [1, 2, 3, 4, 5]
linked_list = copy_list_with_indices(original_list)
print("Original List:")
print(original_list)
print("Linked List:")
print_linked_list(linked_list)
