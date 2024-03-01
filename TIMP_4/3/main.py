def main(expression):
    stack = []
    i = 0

    while i < len(expression):
        if expression[i] == "+":
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(operand2 + operand1)
        elif expression[i] == "*":
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(operand2 * operand1)
        elif expression[i] == "-":  # Добавляем операцию вычитания
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(operand2 - operand1)
        elif expression[i] == "/":  # Добавляем операцию деления
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(operand2 / operand1)
        elif expression[i].isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            stack.append(num)
            continue
        i += 1

    if stack:
        result = stack.pop()
        if not stack:
            return result
        else:
            raise ValueError("Некорректное выражение")
    else:
        raise ValueError("Выражение пустое")


if __name__ == "__main__":
    expression = input("Введите выражение: ")
    try:
        result = main(expression)
        print("Результат:", result)
    except ValueError as e:
        print("Ошибка:", e)
