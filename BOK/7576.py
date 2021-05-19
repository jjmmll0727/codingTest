## tomato - bfs
## 시작점이 여러개인 경우 --> 현재 큐를 보면서 모든 점에서 bfs를 하면 된다 
## 2021.05.19 시간초과...

import sys
col, row = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

queue = list()
visited = list()
dx, dy = [-1,1,0,0], [0,0,1,-1]
start_list = [] ## start하는 좌표들
days = -1
for c in range(row):
    for r in range(col):
        if box[c][r] == 1:
            start_list.append((c,r))
            
def bfs(box, start_list, days):
    while start_list:
        x_list = [0] * len(start_list)
        y_list = [0] * len(start_list)
        days += 1
        for i in range(0, len(start_list)):
            x, y = start_list.pop(0)
            x_list[i] = x
            y_list[i] = y
        for j in range(len(x_list)):
            for i in range(4):
                nx, ny = x_list[j] + dx[i], y_list[j] + dy[i]
                if 0<=nx<row and 0<=ny<col and (box[nx][ny] == 0):
                    start_list.append((nx,ny))
                    box[nx][ny] = 1        
    for b in box:
        if 0 in b:
            return -1
    return days

if __name__ == "__main__":
    print(bfs(box, start_list, days))          
                
