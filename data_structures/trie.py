class Node:
    def __init__(self, num_of_alphabets=26):
        self.mark = False
        self.num_of_alphabets = num_of_alphabets
        self.next_alphabet = [None for i in range(num_of_alphabets)]


def alphabet_to_index(character) -> int:
    asci_char = ord(character)
    if asci_char > ord('z') or asci_char < ord('A'):
        raise Exception("Word cannot have things other than letters.")
    return (ord(character) - 65) % 32  # ord('A') = 65


class Trie:
    def __init__(self, num_of_alphabets=26):
        self.root = Node(num_of_alphabets)

    def __repr__(self):
        pass

    def insert(self, word):
        node = self.root
        for character in word:
            index = alphabet_to_index(character)
            if node.next_alphabet[index] is None:
                node.next_alphabet[index] = Node()
            node = node.next_alphabet[index]
        node.mark = True
        return

    def find(self, word):
        node = self.root
        for character in word:
            index = alphabet_to_index(character)
            if node.next_alphabet[index] is None:
                return False
            node = node.next_alphabet[index]
        return node.mark

    def find_node(self, word):
        node = self.root
        for character in word:
            index = alphabet_to_index(character)
            if node.next_alphabet[index] is None:
                return None
            node = node.next_alphabet[index]
        return node

    def autocomplete(self, incomplete_word):

        # TODO: Find the uncompleted node in case of existence.
        # TODO: Find completed words with DFS.

        if self.find_node(incomplete_word) is None:
            return []



        node = self.root
        for character in incomplete_word:
            pass  # TODO: Do the DFS JOB

    def dfs
