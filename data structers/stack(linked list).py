class Stack:
    class Frame:
        def __init__(self, data, next_frame):
            self.data = data
            self.next_frame = next_frame

    def __init__(self):
        self.items = []
        self.head = None
        self.size = 0

    def push(self, data):
        new_frame = self.Frame(data, self.head)
        self.head = new_frame
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None

        data = self.head.data
        self.head = self.head.next_frame
        self.size -= 1
        return data