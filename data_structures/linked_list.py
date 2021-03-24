class Cell:
    def __init__(self, data, prev, nxt):
        self.data = data
        self.prev = prev
        self.next = nxt

    def change_prev(self, prev):
        self.prev = prev

    def change_next(self, nxt):
        self.next = nxt


class LinkedList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.num = 0
        self.first = None
        self.last = None

    def insert(self, new_data):
        if self.num >= self.max_size:
            raise Exception("Linked List is full.")

        self.num += 1

        # if self.first is None:
        #     self.first = Cell(new_data, None, None)
        # else:
        #     cell = self.first
        #     while cell.next is not None:
        #         cell = cell.next
        #     cell.next = Cell(new_data, cell, None)
        #     return cell.next
        if self.last is None:
            self.first = Cell(new_data, None, None)
            self.last = self.first
        else:
            self.last.next = Cell(new_data, self.last, None)
            self.last = self.last.next
        return self.last

    def get(self, index):
        if self.num <= 0:
            raise Exception("Linked List is empty.")
        elif self.num < index:
            raise Exception("Out of range Linked List.")
        cell = self.first
        self.num -= 1
        for i in range(index - 1):
            cell = cell.next
        result = cell.data
        if cell.prev is not None:
            cell.prev.change_next(cell.next)
        else:
            self.first = None
        del cell
        return result

    def print_ll(self):
        if self.num <= 0:
            print("Linked List is empty.")
            return
        cell = self.first
        while cell is not None:
            print(cell.data, end=" ")
            cell = cell.next
        print()
        return
