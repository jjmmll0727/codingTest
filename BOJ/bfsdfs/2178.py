row, col = map(int, input().split())
matrix = [[0]*(col) for _ in range(row)] ## 만약에 0 이 아닌 []로 채운다면 indexing말고 append로 해야해.
visited = [[0]*(col) for _ in range(row)] ## path count
for i in range(row):
    num = input() ### 처음에 정수형으로 받으면 001 같은 경우는 1로 받아들인다. --> 스트링으로 받아야 해 
    for k in range(col):
        matrix[i][k] = int(num[k]) ## string형식으로 바꾼다음 indexing한 것이 중요!!

dx, dy = [-1,1,0,0], [0,0,1,-1]
queue = [(0,0)] 
visited[0][0] = 1

### bfs 하면서 한번 가면 체크를 하면서 가는 길에 +1 씩 더하면 지나갔던 박스의 갯수를 셀 수 있다. 
while queue:
    nx, ny = queue.pop(0)
    if nx == row-1 and ny == col-1:
        print(visited[nx][ny])
        break
    else: 
        for i in range(4):
            nnx, nny = nx + dx[i], ny + dy[i]
            if 0<=nnx<row and 0<=nny<col:
                if (matrix[nnx][nny] == 1 and visited[nnx][nny] == 0):
                    queue.append((nnx, nny))
                    visited[nnx][nny] = visited[nx][ny] + 1