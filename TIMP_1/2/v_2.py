import numpy as np
import random
import math


def generate_numbers(n, b, r):
    if b:
        return np.random.randint(0, r, n)  # Равномерное распределение
    else:
        random_numbers = np.random.randint(0, r, size=(n, 5))
        return np.mean(random_numbers, axis=1)  # Нормальное распределение


def create_histogram(a, h, r):
    hist, _ = np.histogram(a, bins=np.linspace(0, r, h + 1))
    return hist


def calculate_mode(a):
    value_count = {}  # Словарь для подсчета количества вхождений каждого значения
    for value in a:
        if value in value_count:
            value_count[value] += 1
        else:
            value_count[value] = 1

    max_count = 0
    mode = None
    for value, count in value_count.items():
        if count > max_count:
            max_count = count
            mode = value
    return mode


def calculate_median(a):
    return np.median(a)


def calculate_statistics(a, a2):
    sr = np.mean(a)
    sr_kv = np.std(a)

    print(f"Среднее = {sr}")
    print(f"Мода = {calculate_mode(a)}")
    print(f"Медиана = {calculate_median(a)}")
    print(f"Среднеквадратичное = {sr_kv}")


def display_histogram(a2, h, n):
    print("Гистограмма:")
    n = n // 500
    for count in a2:
        if count < n:
            print("*", end="")
        else:
            for _ in range(count // n):
                print("*", end="")
        print(f" - ({count})")


def main():
    random.seed()
    h = 10
    print("Равномерное распределение rand()")
    b = True
    for r in [10, 100, 1_000]:
        for n in [10_000, 100_000, 1_000_000]:
            print(f"r = {r}; n = {n}")
            a = generate_numbers(n, b, r)
            a2 = create_histogram(a, h, r)
            calculate_statistics(a, a2)
            display_histogram(a2, h, n)

    for i in range(5):
        print()

    print("Нормальное распределение")
    b = False
    for r in [10, 100, 1000]:
        for n in [10_000, 100_000, 1_000_000]:
            print(f"r = {r}; n = {n}")
            a = generate_numbers(n, b, r)
            a2 = create_histogram(a, h, r)
            calculate_statistics(a, a2)
            display_histogram(a2, h, n)


if __name__ == "__main__":
    main()
