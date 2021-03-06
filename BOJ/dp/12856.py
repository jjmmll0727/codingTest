### knapsack algorithm
## spend a lot of time to understand
## 1. 일단 한 물건씩 다 담아본다 (그 물건이 가방의 용량 안에 들아갈 수만 있다면!!!, 그 전에 들어간 물건은 신경 쓰지 않는다.)
## 2. 내가 만약에 이 물건을 넣어서 현재 용량을 만족시키려면, 더 적은 용량의 가방에 들어가 있는 물건들의 가치와 지금 내가 넣는 물건의 가치를 더 해서 
## 3. 현재 용량에 해당하는 가치와 비교한다
## 참고로, 만약에 내가 지금 이 물건을 넣을껀데 아까 넣었던 물건의 용량이 max를 충족시키지 못한다면, 내가 이걸 그냥 추가로 넣어도 되지 않아? 라는 생각은 ㄴㄴ
## 왜냐, 2번 방식을 이용해서 어차피 부족한 용량에서 내가 지금 넣은 물건의 용량을 더해서 결과를 따져볼것이기 때문에.
 
from sys import stdin
from collections import deque
N, K = map(int, stdin.readline().split())
wlist, vlist = deque(), deque()
back = [0] * (K+1) ## 배낭의 용량이 가능한 경우들 
for i in range(N):
    w, v = map(int, stdin.readline().split())
    wlist.append(w)
    vlist.append(v)

for i in range(N):
    for j in range(0, K):
        if K-j >= wlist[i]:
            if back[K-j-wlist[i]]+vlist[i] > back[K-j]:
                back[K-j] = back[K-j-wlist[i]]+vlist[i]

print(max(back))
        
