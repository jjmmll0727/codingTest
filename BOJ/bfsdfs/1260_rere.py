from collections import deque
from sys import stdin

node, line, start = map(int, stdin.readline().split(' '))
matrix = [[]*(node+1) for _ in range(node+1)]
for i in range(line):
    a, b = map(int, stdin.readline().split(' '))
    matrix[a].append(b)
    matrix[b].append(a)
for i in range(node+1):
    matrix[i].sort()

def bfs(matrix, start, node):
    visited = [0] * node
    nodes = deque()
    nodes.append(start)
    ans = []
    while nodes:
        node1 = nodes.popleft()
        if visited[node1-1] == 0 :
            visited[node1-1] = 1
            nodes.extend(matrix[node1])
            ans.append(str(node1))
    print(*ans)

def dfs(matrix, start, node):
    visited = [0] * (node+1)
    nodes = deque()
    nodes.append(start)
    ans = []
    while nodes:
        node1 = nodes.pop()
        if visited[node1] == 0 :
            visited[node1] = 1
            nodes.extend(sorted(matrix[node1], reverse = True))
            ans.append(str(node1))
    print(*ans)

if __name__ == "__main__":
    dfs(matrix, start, node)
    bfs(matrix, start, node)
