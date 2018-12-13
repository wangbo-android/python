from heapq import *
from random import shuffle
from collections import deque

data = list(range(10))
shuffle(data)
print(heapify(data))
heap = []
for n in data:
    heappush(heap, n)
print(heap)
print(heappop(heap))
print(heap)
print(shuffle.__doc__)
print(nlargest(2, heap))
print(nsmallest(2, heap))
d = deque(range(5))
d.append(5)
print(d)
d.appendleft(6)
print(d)
