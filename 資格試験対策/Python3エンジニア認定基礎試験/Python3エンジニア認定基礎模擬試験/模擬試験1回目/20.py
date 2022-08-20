from collections import deque
queue = deque(["bear", "cow", "dog", "elephant","fox"])
queue.append("goat")

queue.pop()
print(queue)
