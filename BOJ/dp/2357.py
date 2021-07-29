from collections import deque
from sys import stdin

nums, combo = map(int, stdin.readline().split())
numlist = list()
maxMinList = deque()
result = deque()

for i in range(nums):
    num = int(stdin.readline().strip('\n'))
    numlist.append(num)
    if i == 0:
        maxMinList.append((num, num))
        maxNum, minNum = num, num
    else:
        if num >= maxNum:
            maxNum = num
        if num <= minNum:
            minNum = num
        maxMinList.append((maxNum, minNum))
numlist.append(num)
maxMinList.append((maxNum,minNum))

result1, result2 = 0, 0
for i in range(combo):
    a, b = map(int, stdin.readline().split())
    if maxMinList[a-1][0] == maxMinList[b-1][0]:
        result1 = max(numlist[a-1:b])
    else:
        result1 = max(maxMinList[a-1][0], maxMinList[b-1][0])
    if maxMinList[a-1][1] == maxMinList[b-1][1]:
        result2 = min(numlist[a-1:b])
    else:
        result2 = min(maxMinList[a-1][1], maxMinList[b-1][1])
    result.append((result2, result1))

for i in range(combo):
    print(result[i][0], result[i][1])