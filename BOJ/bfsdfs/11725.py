## tree 문제인데 탐색을 하는거 봐서 bfs dfs 로 푼다. 
## 이런생각을 할 줄 알아야 해 
## 탐색은 무조건 bfs dfs??
## 정답을 담는 배열로 visited를 판별할 수 있다면 시간을 줄일 수 있다. 

from collections import deque
from sys import stdin

count = int(stdin.readline())
tree = [[]*3 for _ in range(count+1)]
for i in range(count-1):
    num1, num2 = map(int, stdin.readline().split())
    tree[num1].append(num2)
    tree[num2].append(num1)

visited = []
queue = deque()
queue.append(1)
ans = [0] * (count)
ans[0] = 1
while queue:
    q = queue.popleft()
    for i in tree[q]:
        if ans[i-1] == 0:
            queue.append(i)
            ans[i-1] = q

for i in range(count-1):
    print(ans[i+1])


        

