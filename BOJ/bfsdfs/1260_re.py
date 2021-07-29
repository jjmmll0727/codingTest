from collections import deque
from sys import stdin

node, line, start = map(int, stdin.readline().split(' '))

matrix = [[] * (node+1) for _ in range(node+1)]
for i in range(line):
    a, b = map(int, stdin.readline().split(' '))
    matrix[a].append(b)
    matrix[b].append(a)
for i in range(node+1):
    sorted(matrix[i])


def dfs(matrix):
    visited = deque()
    nodes = deque()
    nodes.append(start)
    while nodes:
        n = nodes.popleft()
        if n not in visited:
            visited.append(n)
            nodes.extend(matrix[n])
    return visited


def bfs(matrix):
    visited = deque()
    nodes = deque()
    nodes.append(start)
    while nodes:
        n = nodes.popleft()
        if n not in visited:
            visited.append(n)
            nodes.extend(sorted(matrix[n], reverse = True))
    return visited

if __name__ == "__main__":
    print(dfs(matrix))
    print(bfs(matrix))