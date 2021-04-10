class Node:
    def __init__(self, num_of_alphabets=26):
        self.mark = False
        self.num_of_alphabets = num_of_alphabets
        self.next_alphabet = [None] * num_of_alphabets  # I used to use this: [None for i in range(num_of_alphabets)]


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
            edge_index = alphabet_to_index(character)
            if node.next_alphabet[edge_index] is None:
                node.next_alphabet[edge_index] = Node()
            node = node.next_alphabet[edge_index]
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

    def delete_word(self, word):
        word_node = self.find_node(word)
        if word_node is None:
            raise Exception("Word not found.")
        elif word_node.mark is None:
            raise Exception("Word not found.")
        word_node.mark = False
        return

    def autocomplete(self, incomplete_word) -> []:

        # Done: Find the uncompleted node in case of existence.
        # Done: Find completed words with DFS.

        uncompleted_word_node = self.find_node(incomplete_word)
        if uncompleted_word_node is None:
            return []

        list_of_recommendations = []
        self.autocomplete_dfs(uncompleted_word_node, incomplete_word, list_of_recommendations)
        return list_of_recommendations

    def autocomplete_dfs(self, node, incomplete_word, list_of_recommendations):  # TODO: Is my code DFS or BFS?
        # is_end = True
        for index_num in range(len(node.next_alphabet)):
            if node.next_alphabet[index_num] is not None:
                next_char = index_num + 97  # ord('a') is 97.
                next_incomplete_word = incomplete_word + chr(next_char)
                self.autocomplete_dfs(node.next_alphabet[index_num], next_incomplete_word, list_of_recommendations)
                # is_end = False
        if node.mark is True:
            list_of_recommendations.append(incomplete_word)

