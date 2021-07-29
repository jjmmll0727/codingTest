if __name__ == "__main__":
    count, total = map(int, input().split())
    listt = list(map(int, input().split()))
    temp = 0
    for i in range(count):
        for j in range(i+1, count):
            for k in range(j+1, count):
                sum = listt[i]+listt[j]+listt[k]
                if (sum <= total) and (sum > temp):
                    temp = sum
    print(temp)
    
