# 영화감독 숌
# brute force 알고리즘

order = int(input())
terminal = 666
count = 1

while True:
    if order == 1:
        print(terminal)
        break
    terminal = terminal + 1
    if '666' in str(terminal):  
        count = count + 1
        if order == count:
            print(terminal)
            break
        