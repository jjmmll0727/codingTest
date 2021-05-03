def counting(num):
    count = 0
    total = num
    if num < 10:
        return num, 1
    else:
        while num > 0:
            total = total + num % 10
            num = num // 10
            count = count + 1
        return total, count

if __name__ == "__main__":
    sumof = int(input()) 
    ans = sumof                         
    sumof = sumof - len(str(sumof))*9  
    while True:
        c, d = counting(sumof)
        if c == ans:
            print(sumof)
            break
        sumof = sumof + 1