## 정렬문제 
## 파이썬의 sort함수는 timsort라는 그 동안의 정렬 알고리즘의 약점을 보완한 알고리즘이라 속도가 상당히 빠르다... 이런 파이썬 이쁜놈 ㅋㅋ
## 여기서 파이썬의 좋은 기능을 알 수 있다. 
## 1. set함수는 중복을 제거해준다. 다시 list화 하면 돌아온다
## 2. sort key=lambda x:()

from collections import deque
from sys import stdin

count = int(stdin.readline())
strlist = deque()
for i in range(count):
    strlist.append(stdin.readline().rstrip("\n"))
uniqlist = list(set(strlist)) ## 중복제거한 리스트 
uniqlen = len(uniqlist)
anslist = [[0] * 2 for _ in range(uniqlen)]

for i in range(uniqlen):
    anslist[i][0] = uniqlist[i] 
    anslist[i][1] = len(uniqlist[i])

anslist.sort(key=lambda x:(x[1], x[0]))
for i in range(uniqlen):
    print(anslist[i][0])
