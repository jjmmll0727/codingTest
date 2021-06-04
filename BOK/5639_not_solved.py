## 이진탐색트리형성
from sys import stdin
from collections import deque

tree = {}
nodes = deque()
while True:
    try:
        node = int(stdin.readline())
    except:
        break
    nodes.append(node)

    

