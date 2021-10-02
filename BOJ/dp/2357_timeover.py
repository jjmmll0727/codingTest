from collections import deque
from sys import stdin

nums, combo = map(int, stdin.readline().split())
numlist = list()
result = deque()

for i in range(nums):
    num = int(stdin.readline().strip('\n'))
    numlist.append(num)
for i in range(combo):
    maxNum, minNum = 0, 0
    a, b = map(int, stdin.readline().split())
    maxNum, minNum = numlist[a-1], numlist[b-1]
    for j in range(a,b):
        if numlist[j] > maxNum:
            maxNum = numlist[j]
        elif numlist[j] < minNum:
            minNum = numlist[j]
    result.append((minNum, maxNum))

for i in range(combo):
    print(result[i][0], result[i][1])

### 이렇게 풀면 시간초과
### 세그먼트 트리로 풀어야 한다.

