from collections import deque

d = deque(["task1", "task2"])
print(d)

d.append("task3")
print(d)

d.appendleft("task4")
print(d)
