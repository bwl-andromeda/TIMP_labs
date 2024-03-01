import random
import math


class Point:
    def __init__(self, coords):
        self.coords = coords


def rand_float():
    return random.uniform(0, 1.0)


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a.coords, b.coords)))


def main(N, d):
    random.seed()
    points = [Point([rand_float() for _ in range(d)]) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(i + 1, N):
            if distance(points[i], points[j]) < 1.0:
                cnt += 1

    print(f"{cnt} пар внутри 1.0")


if __name__ == "__main__":
    N = int(input("Введите количество точек (N): "))
    d = int(input("Введите размерность (d): "))
    main(N, d)
