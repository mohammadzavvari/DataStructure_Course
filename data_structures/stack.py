class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.S = [0] * self.max_size
        self.up = 0
        # self.num = 0 We do not need it.

    def push(self, new_data):
        if self.up >= self.max_size:  # We use >= to ensure that nothing went wrong (Usually by using "unsigned int").
            raise Exception("Stack is full.")
        self.S[self.up] = new_data
        self.up += 1
        # self.num += 1
        return

    def pop(self):
        if self.up <= 0:
            raise Exception("Stack is empty.")
        self.up -= 1
        # self.num -= 1
        return self.S[self.up]
