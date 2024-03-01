def copy_list_with_indices(input_list):
    # Создаем массив индексов
    indices = list(range(len(input_list)))

    # Создаем новый список, используя генератор списка
    copied_list = [input_list[i] for i in indices]

    return copied_list


# Пример использования:
original_list = [1, 2, 3, 4, 5]
copied_list = copy_list_with_indices(original_list)
print(copied_list)
