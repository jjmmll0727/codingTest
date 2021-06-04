## dfs bfs 
## 일차원 평면에서도 dfs, bfs 를 사용한다. 
## 시간초과 뜬 이유 --> not in visited 형식은 데큐를 한번 쭉 훑어야 해서 O(n) 만큼의 시간이 소요
## 하지만 true, false 형식이면 O(1) 시간안에 가능하다. 

from sys import stdin
from collections import deque
N, K = map(int, stdin.readline().split())
count = 0
roads = deque([[N, count]])
visited = [False] * 100001

while roads:
    sc = roads.popleft()
    start = sc[0]
    count = sc[1]
    if visited[start] == False:
        visited[start] = True
        if start == K:
            print(count)
            break
        count += 1
        if start + 1 <= 100000:
            roads.append([start+1,count])
        if start - 1 >= 0:
            roads.append([start-1,count])
        if start * 2 <= 100000:
            roads.append([start * 2,count])


