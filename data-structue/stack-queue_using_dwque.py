from collections import deque

q= deque([1,2,3,4,5,6,7,8,9])

# pop(), popleft(), append(), appendleft()

# poping element

print(q)
print(q.pop())
print(q)
print(q.popleft())
print(q)

# inserting element

print(q)
q.append(10)
print(q)
q.appendleft(-1)
print(q)