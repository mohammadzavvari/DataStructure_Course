from .trie import *


def main():
    trie = Trie()
    trie.insert("Hello")
    trie.insert("Bye")
    trie.insert("salaam")
    trie.insert("D")
    trie.insert("de")
    trie.insert("Dera")
    trie.insert("derakht")
    trie.insert("derakhshan")
    trie.insert("derderder")

    print(trie.find('d'))
    print(trie.find("D"))
    print(trie.find("de"))
    print(trie.find("Dera"))
    print(trie.find("derakht"))
    print(trie.find("derakhshan"))
    print(trie.find("derderder"))



    word_search = input()
    print(trie.autocomplete(word_search))
