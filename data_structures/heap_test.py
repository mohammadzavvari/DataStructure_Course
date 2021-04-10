from .heap import Heap


def main():
    heap = Heap()
    print(repr(heap))

    heap.insert(2)
    print(repr(heap))

    heap.insert(4)
    print(repr(heap))

    heap.insert(7)
    print(repr(heap))

    heap.insert(3)
    print(repr(heap))

    heap.insert(8)
    print(repr(heap))

    heap.insert(10)
    print(repr(heap))
