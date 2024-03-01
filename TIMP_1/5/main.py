import random


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Генерируем случайные две пары чисел с плавающей точкой от 0 до 1
width1 = random.uniform(0, 1)
height1 = random.uniform(0, 1)
width2 = random.uniform(0, 1)
height2 = random.uniform(0, 1)

# Создаем прямоугольники
rectangle1 = Rectangle(width1, height1)
rectangle2 = Rectangle(width2, height2)

# Вычисляем площади прямоугольников
area1 = rectangle1.area()
area2 = rectangle2.area()

# Вычисляем среднюю площадь сгенерированных прямоугольников
average_area = (area1 + area2) / 2

print("Площадь первого прямоугольника:", area1)
print("Площадь второго прямоугольника:", area2)
print("Средняя площадь сгенерированных прямоугольников:", average_area)
