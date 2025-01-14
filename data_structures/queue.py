import collections

q = collections.deque()

element = 115

# Такой вариант позволяет реализовывавать методы:
q.append(element)
element = q.pop()
element = q.popleft()
q.appendleft(element)
# за O(1) операций