class Node:
    def __init__(self, num_of_alphabets=26):
        self.mark = False
        self.num_of_alphabets = num_of_alphabets
        self.next_alphabet = [None for i in range(num_of_alphabets)]


def alphabet_to_index(character):
    return (ord(character) - 65) % 32  # ord('A') = 65


class Trie:
    def __init__(self, num_of_alphabets=26):
        self.root = Node(num_of_alphabets)

    def __repr__(self):
        pass

    def insert(self, word):
        # length = len(word)
        node = self.root
        for character in word:
            index = alphabet_to_index(character)
            if node.next_alphabet[index] is None:
                node.next_alphabet[index] = Node()
            node = node.next_alphabet[index]
        node.mark = True
        return
