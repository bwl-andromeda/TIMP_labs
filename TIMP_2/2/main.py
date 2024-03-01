import random
def is_square_or_cube(num):
    square_root = int(num**0.5)
    cube_root = int(num ** (1 / 3))

    if square_root**2 == num or cube_root**3 == num:
        return True
    else:
        return False


def count_numbers(n = int(input("Введите кол-во симуляций: "))):
    counts = {}

    for _ in range(n):
        count = 0

        while True:
            num = random.randint(1, 999)
            count += 1

            if is_square_or_cube(num):
                break

        if count in counts:
            counts[count] += 1
        else:
            counts[count] = 1

    return counts


def print_histogram():
    print("Гистограмма:")
    sorted_counts = sorted(count_numbers().items(), key=lambda x: x[0])
    for key, value in sorted_counts:
        stars = "*" * value
        print(f"{key}: {stars} - ({value})")


print_histogram()
