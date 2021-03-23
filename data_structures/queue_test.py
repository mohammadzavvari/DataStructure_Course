from data_structures.queue import Queue

q = Queue(10)
print(repr(q))
for i in range(10):
    q.enqueue(i+1)
print(repr(q))
q.dequeue()
print(repr(q))
q.dequeue()
print(repr(q))
q.enqueue(-1)
print(repr(q))
for i in range(10):
    q.dequeue()
    print(repr(q))
