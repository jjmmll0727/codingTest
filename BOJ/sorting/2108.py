## simple sorting
## dictionary 는 sort를 제공하지 않는다. --> sorted 함수르르 사용해야 해 

from sys import stdin
from collections import deque

## 산술기하
def meanOfSum(numlist):
    if sum(numlist)/listlen - 0.5 >= sum(numlist)//listlen:
        return sum(numlist)//listlen + 1
    else:
        return sum(numlist)//listlen

##  중간값
def middle(numlist):
    temp = sorted(numlist)
    return temp[listlen // 2]

## 최빈값 - 2개 이상이면 두번째로 작은 수
def most(numlist):
    mostlist = {}
    for i in range(listlen):
        if numlist[i] not in mostlist:
            mostlist[numlist[i]] = 0
        mostlist[numlist[i]] += 1
    #temp = sorted(mostlist.items(), key = lambda x: (x[1]), reverse=True)
    temp = sorted(mostlist.items(), key = lambda x : (-x[1], x[0]))
    if len(temp) == 1:
        return temp[0][0]
    else: ## 원소가 한개가 아닌 경우
        if temp[0][1] == 1: ## 첫번째 원소가 1이다? 최다 빈도 횟수가 1이다 --> 모든 빈도수가 1이다.
            return temp[1][0]
        else: 
            if temp[0][1] == temp[1][1]:
                return temp[1][0]
            else:
                return temp[0][0]

## 최대값과 최솟값의 차이
def minus(numlist):
    temp = sorted(numlist)
    return temp[-1] - temp[0]

if __name__ == '__main__':
    count = int(stdin.readline())
    numlist = list()
    for i in range(count):
        num = int(stdin.readline())
        numlist.append(num)
    listlen = len(numlist)

    print(meanOfSum(numlist))
    print(middle(numlist))
    print(most(numlist))
    print(minus(numlist))