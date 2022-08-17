[ 実行結果 ]
deque(['cow', 'dog', 'elephant', 'fox'])

[ コード ]
from 【A】 import deque
queue = deque(["bear", "cow", "dog", "elephant","fox"])
queue.append("goat")
【B】
queue.pop()
print(queue)
