from sys import stdin
if __name__ == "__main__":
    num = int(stdin.readline())
    ans = 0
    for i in range(1, num+1):
        temp = sum(list(map(int, str(i))))
        if i+temp == num:
            ans = i
            break
        
    print(ans)