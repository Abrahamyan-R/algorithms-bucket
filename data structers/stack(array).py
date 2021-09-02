class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size
        self.top = 0

    def push(self, data):
        if self.top == self.size:
            raise ValueError("Stack is full")

        self.items.append(data)
        self.top += 1

    def pop(self):
        if self.top == 0:
            raise ValueError("Stack is empty")

        self.top -= 1
        return self.items.pop()