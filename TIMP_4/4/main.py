class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def error(self, message):
        print(f"Error: {message}")

    def enqueue(self, item):
        if self.is_full():
            self.error("Queue is full. Cannot enqueue.")
            return
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            self.error("Queue is empty. Cannot dequeue.")
            return None
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.capacity
            return temp

    def first(self):
        if self.is_empty():
            self.error("Queue is empty. No first element.")
            return None
        return self.queue[self.front]

    def last(self):
        if self.is_empty():
            self.error("Queue is empty. No last element.")
            return None
        return self.queue[self.rear]

    def dump(self):
        if self.is_empty():
            self.error("Queue is empty.")
            return
        index = self.front
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        print()

    def clear(self):
        self.front = self.rear = -1

    def count(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.capacity - self.front + self.rear + 1


# Пример использования
if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Queue contents:")
    q.dump()

    print(f"First element: {q.first()}")
    print(f"Last element: {q.last()}")
    print(f"Queue count: {q.count()}")

    q.dequeue()
    print("Queue contents after dequeuing:")
    q.dump()

    q.clear()
    print("Queue cleared. Is it empty now?", q.is_empty())
