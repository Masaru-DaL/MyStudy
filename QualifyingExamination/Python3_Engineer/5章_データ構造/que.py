from collections import deque

queue = deque(["hello", "world"])
queue.append("Python")
print(queue)

print(queue.popleft())
print(queue)
