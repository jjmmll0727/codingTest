from collections import deque
from sys import stdin

def bfs(roads, start): 
    nx, ny = 0, 0
    while start:
        x, y, c = start.popleft() 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] 
            if (0<=nx<xx and 0<=ny<yy): 
                if roads[nx][ny] == 0 and ans[nx][ny][c] == 0:
                    start.append((nx,ny,c))               
                    ans[nx][ny][c] = ans[x][y][c] + 1 
                elif roads[nx][ny] == 1 and c == 0 and ans[nx][ny][c] == 0: # 벽이 있어 그런데 한번도 부셔본적이 없다면 부셔봐라.
                                                                            # 여기서 시간복잡도를 줄였는데, visited 배열을 쓰지 않고,
                                                                            # ans 배열에 z성분이 0이면 한번도 가지 않은 곳이다. 
                                                                            # 앞으로 2차원 배열에서 계산할때도 따로 visited 배열을 사용하지 않고, 
                                                                            # 정답을 기록하는 배열을 이용하면 시간복잡도를 더 줄일 수 있을 것이다. 
                    start.append((nx,ny,1))                
                    ans[nx][ny][1] = ans[x][y][c] + 1
            if nx == xx-1 and ny == yy-1:
                return max(ans[nx][ny][0]+1, ans[nx][ny][1]+1) ## 마지막 위치는 가지는 않은 상태. 확인만 한 상태이기 때문에 +1 해준다
    return -1

if __name__ == "__main__":
    xx, yy = map(int, stdin.readline().split())
    start = deque()
    ans = [[[0] * 2 for _ in range(yy)] for _ in range(xx)]
    roads = [[0] * yy for _ in range(xx)]
    for i in range(xx):
        num = stdin.readline()
        for j in range(yy):
            roads[i][j] = int(str(num)[j]) ## map setting
    start.append((0,0,0))
    dx, dy = [-1,1,0,0], [0,0,1,-1]
    if xx == 1 and yy == 1: ## map의 크기가 1X1 인 경우(출발점과 도착점이 같은 경우를 고려해줘야 한다)
        print('1')
    else:
        print(bfs(roads, start))


    