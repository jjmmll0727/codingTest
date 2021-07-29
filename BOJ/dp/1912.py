## 답 리스트에 첫번쨰 원소값을 넣고, numlist와 더하면서 만약에 음수가 나오면 0을 답리스트에 추가하고, 그렇지 않으면 더한 값을 추가한다.

from sys import stdin
from collections import deque

count = int(stdin.readline())
numlist = list(map(int, stdin.readline().split()))
zerocount = 0 ## 입력받는 원소중 0이하의 갯수 만약에 모두다 0이하면 계산을 할 필요없이 무조건 가장큰수를 출력하면 돼 

for i in range(count):
    if numlist[i] <= 0:
        zerocount += 1
if zerocount == count:
    print(max(numlist))
else:
    ans = deque()
    ans.append(numlist[0])
    for i in range(count-1):
        if numlist[i] < 0:
            zerocount += 1
        if numlist[i+1] + ans[i] < 0:
            ans.append(0)
        else:
            ans.append(numlist[i+1] + ans[i])
    print(max(ans))
