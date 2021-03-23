class Queue:
    """
        This class is a Queue data structure,
        It has two pointers for beginning and end of data in queue.
    """
    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * self.max_size
        self.num = 0
        self.first = 0

    def __repr__(self):
        representation = ""
        for i in range(self.num):
            representation += str(self.Q[(self.first + i) % self.max_size])
            if i != self.num - 1:
                representation += ", "
        return representation

    def enqueue(self, new_data):
        if self.num >= self.max_size:  # We use >= to ensure that nothing went wrong (Usually by using "unsigned int").
            raise Exception("Queue is full.")

        # if self.num + self.first == self.max_size:
        #     self.shift_queue()

        self.Q[(self.num + self.first) % self.max_size] = new_data
        self.num += 1
        return

    def dequeue(self):
        if self.num <= 0:
            raise Exception("Queue is empty.")

        result = self.Q[self.first]
        # if self.first == self.max_size - 1:
        #     self.first = 0
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        return result

    def shift_queue_simple(self):
        self.first -= -1
        for i in range(self.first, self.max_size - 1):
            self.Q[i] = self.Q[i + 1]
        return

    def shift_queue(self):
        for i in range(self.num):
            self.Q[i] = self.Q[self.first + i]
        self.first = 0
        return
