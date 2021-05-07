# 동전문제 
# 그리디 알고리즘
# 동적 프로그래밍을 보완하기 위한 알고리즘으로, 현재의 상황에서 최선의 선택을 한다면 결과적으로 좋은 결과가 나올 것이라는 예상을 하는 알고리즘

total_coin, total_val = map(int, input().split())
coin_list = []
total_count = 0
for i in range(total_coin):
    val = int(input())
    coin_list.append(val)

coin_list.reverse()
for i in range(total_coin):
    if coin_list[i] <= total_val: 
        count =  total_val // coin_list[i]
        total_count = total_count + count
        total_val = total_val - count * coin_list[i]
print(total_count)