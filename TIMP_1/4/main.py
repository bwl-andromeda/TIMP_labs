import math

yes = "Да"
No = "Нет"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        dist = math.sqrt(dx * dx + dy * dy)
        return dist

    def is_close_to(self, other, tolerance=1e-4):
        dist = self.distance(other)
        return dist <= tolerance


# Пример использования
point1 = Point(0.5, 0.5)
point2 = Point(0.6, 0.6)

distance = point1.distance(point2)
is_close = point1.is_close_to(point2, tolerance=1e-4)

print(f"Расстояние между точкой 1 и точкой 2: {distance}")
print(f"Близка ли точка 1 к точке 2 в пределах допуска? {yes if is_close else No}")
