from collections import deque
from sys import stdin

y, x = map(int, stdin.readline().split(' '))
matrix = [[]*x for _ in range(y)]
for i in range(y):
    temp = stdin.readline()
    for j in range(x):
        matrix[i].append(int(str(temp)[j]))

visited = [[0]* x for _ in range(y)]
dx, dy = [0,0,1,-1], [1,-1,0,0]
nodes = deque()
nodes.append((0,0))
while nodes:
    a, b = nodes.popleft()
    for i in range(4):
        ax, by = a + dx[i], b + dy[i]
        if 0<=ax<x and 0<=by<y:
            if matrix[by][ax] == 1 and visited[by][ax] == 0:
                visited[by][ax] = visited[b][a] + 1
                nodes.append((ax,by))
print(visited[y-1][x-1]+1)
