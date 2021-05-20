## dynamic programming

from sys import stdin
from collections import deque

count = int(stdin.readline())
numlist = list(map(int, stdin.readline().split()))
ans = [1] * len(numlist)

for i in range(len(numlist)):
    for j in range(i):
        if numlist[i] > numlist[j]:
            ans[i] = max(ans[i], ans[j]+1)
print(max(ans))