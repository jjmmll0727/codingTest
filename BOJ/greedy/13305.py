#주유소
"""
전형적인 greedy 문제
이러한 문제는 최솟값 혹은 최댓값을 주기적으로 초기화 시켜주는 방법을 생각하면 된다. 
어려운 문제.
"""
city_count = int(input())
value_sum = 0
roads = list(map(int, input().split()))
values = list(map(int, input().split()))
min_val = values[0]

for i in range(city_count-1):
    if min_val > values[i]:
        min_val = values[i]
    value_sum += min_val * roads[i]
print(value_sum)
    

