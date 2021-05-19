## tomato - bfs
## 시작점이 여러개면 그 갯수만큼 한다음에 행렬의 차(절댓값)로 계산하면 될듯 
col, row = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(row)]

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
        x,y = start_list.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<row and 0<=ny<col and (box[nx][ny] == 0):
                start_list.append((nx,ny))
                box[nx][ny] = 1
        days += 1
                
    for b in box:
        if 0 in b:
            return -1
    return days

if __name__ == "__main__":
    print(bfs(box, start_list, days))          
                
