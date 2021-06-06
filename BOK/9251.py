## 동적계획법
## LCS - longest common subsequence
## 동적계획법은 이차원 배열을 자주 사용한다 !!!
## 뻘짓 했다. 
## 나는 같은 경우 - max(wordmap[i][j], wordmap[i][j+1], wordmap[i+1][j]) + 1
## 다른 경우 - max(wordmap[i][j], wordmap[i][j+1], wordmap[i+1][j]) 
## 이렇게 했지만 잘못된 방법이었다. 
## sass / sas 를 비교하면 4라는 값이 나왔다.
## 고로, 같은 경우 - wordmap[i][j] + 1
## 다른 경우 - max(wordmap[i][j+1], wordmap[i+1][j])
## 이렇게 해야한다. 
## 처음에 입력받는 문자열의 길이를 비교할 필요가 없었다. 

from sys import stdin

word1 = stdin.readline()
word2 = stdin.readline()

w1len = len(word1)
w2len = len(word2)
wordmap = [[0] * (w1len) for _ in range(w2len)]
for i in range(w2len-1): 
    for j in range(w1len-1):
        if word2[i] == word1[j]:
            wordmap[i+1][j+1] = wordmap[i][j] + 1
        else:
            wordmap[i+1][j+1] = max(wordmap[i][j+1], wordmap[i+1][j])
print(wordmap[w2len-1][w1len-1])

    