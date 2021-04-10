class Node:
    def __init__(self):
        self.mark = False
        self.edges = [None] * 26  # A list of Edges exiting from this node


def trie_insert(node, string, idx=0):
    if idx == len(string):
        node.mark = True  # marking the node
        return
    e = ord(string[idx]) - ord('a')  # alphabet_to_index() in my code
    if node.edges[e] is None:
        node.edges[e] = Node()
    trie_insert(node.edges[e], string, idx + 1)


def trie_search(node, string, idx=0):
    if idx == len(string):
        return node.mark
    e = ord(string[idx]) - ord('a')  # alphabet_to_index() in my code
    if node.edges[e] is None:
        return False
    return trie_search(node.edges[e], string, idx + 1)


def trie_delete(node, string, idx=0):
    if idx == len(string):
        if node.mark is False:
            raise Exception("Item not found")
        node.mark = False
        return
    e = ord(string[idx]) - ord('a')
    if node.edges[e] is None:
        raise Exception("Item not found")
    trie_delete(node.edges[e], string, idx + 1)
