class Node:
    def __init__(self, number):
        self.number = number
        self.parent = None
        self.lower_child = None
        self.higher_child = None


# This tree is not a heap. It is improved BST.
class Heap_v1:  # This Heap hold maximum at the top.
    def __init__(self, first_number):
        self.top = Node(first_number)

    def insert(self, insert_number, node):
        if insert_number >= node.number:
            inserted_node = Node(insert_number)
            inserted_node.parent = node.parent
            inserted_node.higher_child = node.higher_child
            inserted_node.left_child = node
            node.parent = inserted_node
            node.higher_child = None
            return inserted_node

        if node.lower_child is None:
            inserted_node = Node(insert_number)
            inserted_node.parent = node
            node.lower_child = inserted_node
            return inserted_node

        return self.insert(insert_number, node.lower_child)

    def get_top(self):
        return self.top.number

    def delete_top(self):
        # old_top = self.top
        # if old_top.higher_child is not None:  # Top should not have higher child.
        #     raise Exception("Top has higher child.")
        # self.top = old_top.lower_child
        # if self.top is not None:
        #     self.top.parent = None
        # del old_top
        # return self.top
        if self.top.lower_child is None:
            del self.top
            return None

        new_top = self.find_next_top(self.top.lower_child)

        if new_top.parent is self.top:
            del self.top
            self.top = new_top
            self.top.parent = None
            return self.top

        if new_top.lower_child is not None:
            new_top.lower_child.parent = new_top.parent

        new_top.parent.higher_child = new_top.lower_child
        new_top.parent = None
        new_top.lower_child = self.top.lower_child
        new_top.lower_child.parent = new_top
        del self.top
        self.top = new_top
        return self.top

    def find_next_top(self, node):
        if node.higher_child is not None:
            return self.find_next_top(node.higher_child)
        return node

    def pop_top(self):
        top = self.get_top()
        self.delete_top()
        return top


# class Heap:
#     def __init__(self):
#         self.heap = []
#         self.first_empty_index = 1
#
#     def insert(self, number):
#         self.heap[self.first_empty_index] = number
#         parent_index = self.first_empty_index // 2
#         while self.heap[parent_index] > self.heap[self.first_empty_index]:
#             self.heap[parent_index], self.heap[self.first_empty_index] = \
#                 self.heap[self.first_empty_index], self.heap[parent_index]
#         self.first_empty_index += 1
#         return
#
#     def delete_top(self):
#         if self.heap[self.first_empty_index] == 1:
#             return None
#         if self.heap[2] > self.heap[3]:
#             self.heap[1] = self.heap[2]
#         else:
#             self.heap[1] = self.heap[3]
#
#
#     def get_top(self):
#         return self.heap[1]
#
#     def pop_top(self):
#         top = self.get_top()
#         self.delete_top()
#         return top
