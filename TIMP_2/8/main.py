def print_words_in_column(input_string):
    # Разделите строку на слова, используя пробел в качестве разделителя
    words = input_string.split()

    # Выводим каждое слово в столбик
    for word in words:
        print(word)


# Запросите у пользователя ввод строки
input_string = input("Введите строку: ")

# Вызовем функцию для вывода слов в столбик
print_words_in_column(input_string)
