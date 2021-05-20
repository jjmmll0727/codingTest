## tomato - bfs
## 시작점이 여러개인 경우 --> 현재 큐를 보면서 모든 점에서 bfs를 하면 된다 여기서는 전단계에서 추가된 토마토만을 대상으로 bfs를 진행하였다. 
## 2021.05.19 시간초과...
## 원인은 바로 deque 
## list로 구현하는 것 보다 deque로 구현하는것이 훨씬 빠르다. 반드시 deqeu를 통해서 popleft로 구현할 것!!!!

import sys
from collections import deque 
col, row = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]

dx, dy = [-1,1,0,0], [0,0,1,-1]
start_list = deque() ## start하는 좌표들
days = 0
for c in range(row):
    for r in range(col):
        if box[c][r] == 1:
            start_list.append((c,r))
            
def bfs(box, start_list, days):
    while True:
        start_temp = deque()
        while start_list:
            x, y = start_list.popleft()
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0<=nx<row and 0<=ny<col and (box[nx][ny] == 0):
                    start_temp.append((nx,ny))
                    box[nx][ny] = 1  
        start_list = start_temp ## 이렇게 하는 것이 이중 for 사용하지 않고 더 빠르게 해결할 수 있다. 
        if not start_list:
            break
        days += 1      
    for b in box:
        if 0 in b:
            return -1
    return days

if __name__ == "__main__":
    print(bfs(box, start_list, days))          
                
