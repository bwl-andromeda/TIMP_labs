import random
import math


def generate_numbers(n, b, r):
    a = []
    for i in range(n):
        num = 0
        if b:
            num = random.randint(0, r - 1)  # Равномерное распределение
        else:
            for _ in range(5):
                num += random.randint(0, r - 1)
            num /= 5.0  # Нормальное распределение
        a.append(num)
    return a


def create_histogram(a, h, r, n):
    a2 = [0] * (h + 1)
    y = 0
    s = float(r) / h

    for i in range(h + 1):
        for j in range(n):
            if y <= a[j] < y + s:
                a2[i] += 1
        y += s

    a3 = [0] * r
    for i in range(r):
        for j in range(n):
            if a[j] == i:
                a3[i] += 1

    return a2, a3


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
    n = len(a)
    a.sort()
    if n % 2 == 1:
        median = a[n // 2]
    else:
        i = n // 2
        median = (a[i] + a[i + 1]) / 2
    return median


def calculate_statistics(a, a2, a3, n, h, r):
    sr = sum(a) / n
    sr_kv = math.sqrt(sum((sr - x) ** 2 for x in a) / n)

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
            a.sort()
            a2, a3 = create_histogram(a, h, r, n)
            calculate_statistics(a, a2, a3, n, h, r)
            display_histogram(a2, h, n)

    print("Нормальное распределение")
    b = False
    for r in [10, 100, 1000]:
        for n in [10000, 100000, 1_000_000]:
            print(f"r = {r}; n = {n}")
            a = generate_numbers(n, b, r)
            a2, a3 = create_histogram(a, h, r, n)
            calculate_statistics(a, a2, a3, n, h, r)
            display_histogram(a2, h, n)


if __name__ == "__main__":
    main()
