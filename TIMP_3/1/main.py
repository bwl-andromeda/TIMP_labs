def fill_array(n):  # создаём функцию fill_array(n) где n - размерность массива.
    def is_coprime(a, b):  # функция проверяет, что число a и b взаимно простые используя алгоритм Евклида.
        while b != 0:
            a, b = b, a % b
        return a == 1

    array = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if is_coprime(i, j):  # Если i and j простые, то установим значение элемента - 1.
                array[i][j] = 1

    return array # Возвращаем массив.


n = int(input("Введите размерность массива: "))
result = fill_array(n)
for row in result:
    print(row)
