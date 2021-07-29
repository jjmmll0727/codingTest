### 1인 지점만 갈 수 있다. 
from collections import deque
from sys import stdin

row, col = map(int, stdin.readline().split())
matrix = [[] * col for _ in range(row)]

for i in range(row):
    road = stdin.readline()
    for j in range(col):
        matrix[i].append(int(str(road)[j]))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1 ,-1]

visited = [[0] * col for _ in range(row)]
nodes = deque()
nodes.append((0,0))
while nodes:
    x, y = nodes.popleft()
    for i in range(4):
        rx, ry = x + dx[i], y + dy[i]
        if 0 <= rx < col and 0 <= ry < row:
            if matrix[ry][rx] == 1 and visited[ry][rx] == 0:
                nodes.append((rx, ry))
                visited[ry][rx]  = visited[y][x] + 1
print(visited[row-1][col-1]+1)
