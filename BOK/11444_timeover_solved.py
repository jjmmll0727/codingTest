## 피보나치 수열
## 분할 정복
## 기본적으로 피보나치 수열을 풀려고 하면 재귀를 사용하는데 오버플로우가 발생할 수 있다. 
## 그렇기 때문에 분할정복을 사용하는데, 피보나치 수열을 푸는데 있어서 가장 빠른 방법이라고 할 수 있다. 

from sys import stdin

def pibo(n):
    if n<=1:
        return init
    else:
        temp = pibo(n//2) ## key point --> 어떠한 함수를 부르는 연산은 미리 변수 선언을 해놓고 그 변수를 부르는것이 시간적으로 단축 가능!!
        if n%2 == 0:
            return SumOfProduct( temp, temp)
        else:
            return SumOfProduct( init, SumOfProduct(temp, temp))

def SumOfProduct(matrix1, matrix2):
    
    ans = [[0] * 2 for _ in range(2)]
    ans[0][0] = (matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0])%1000000007
    ans[0][1] = (matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1])%1000000007
    ans[1][0] = (matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0])%1000000007
    ans[1][1] = (matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1])%1000000007

    return ans
    
if __name__ == "__main__":
    num = int(stdin.readline())
    init = [[0,1],[1,1]]
    if num == 0:
        print("0")
    else:
        print(pibo(num)[0][1])
        

"""

import sys 
c = 1000000007 
def multiply(matrix1, matrix2): # 행렬의 곱셈 함수 
    ans = [] 
    for i in range(len(matrix1)): 
        ans.append([]) 
        for j in range(len(matrix2[0])): 
            temp = 0 
            for k in range(len(matrix1[0])): 
                temp += matrix1[i][k] * matrix2[k][j] 
            ans[i].append(temp % c) 
    return ans 

def power(matrix, p): # 행렬의 거듭제곱 함수 
    if p == 1: 
        return matrix 
    else: 
        temp = power(matrix, p // 2) 
        if p % 2 == 0: 
            return multiply(temp, temp) 
        else: 
            return multiply(multiply(temp, temp), matrix) 
        
n = int(sys.stdin.readline()) 
m = [[1, 1], [1, 0]] 
print(power(m, n)[0][1])

"""