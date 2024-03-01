class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None


def process_string(input_string):
    stack = Stack()
    result = []

    for char in input_string:
        if char == "*":
            popped = stack.pop()
            if popped is not None:
                result.append((popped, " ".join(stack.items[::-1])))
        else:
            stack.push(char)
            result.append(("", " ".join(stack.items[::-1])))

    return result


input_string = input("Введите строку: ")
processed_string = process_string(input_string)

for item in processed_string:
    print(f"{item[0]:<5}{item[1]}")
