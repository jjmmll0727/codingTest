## 문제를 보고 brute-force 로 풀까 생각하고 너무 시간복잡도가 많아 보이던가 memorization을 활용할 수 있다고 생각하면 DP를 생각해라.
## 코딩문제는 수능29, 30번 처럼 엄청나게 기발한 아이디어를 요구하지는 않는다. 
## 점화식을 생각하자 대신 관계를 앞뒤로 모두 확인해야 해 

from sys import stdin
from collections import deque

def wine(numlist, i):    
    if i < 2:
        ans[i] = sum(numlist)
    elif i == 2:
        templist = numlist.copy()
        temp1 = max(templist)
        templist.remove(temp1)
        temp2 = max(templist)
        ans[i] = temp1 + temp2
    else:
        ch1 = numlist[i] + ans[i-2]
        ch2 = numlist[i] + numlist[i-1] + ans[i-3]
        ch3 = ans[i-1]
        ans[i] = max(ch1, ch2, ch3)

if __name__ == "__main__":
    count = int(stdin.readline())
    numlist = deque()
    ans = [0] * count
    for i in range(count):
        numlist.append(int(stdin.readline()))
        wine(numlist, i)
    print(ans[count-1])