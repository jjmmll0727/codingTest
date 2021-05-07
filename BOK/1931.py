# 회의실 배정
# 그리디 

meeting = int(input())
meeting_list = []
count = 1 #회의는 반드시 1개 이상 
for i in range(meeting):
    start, end = map(int, input().split())
    meeting_list.append([start , end]) #파이썬의 엄청난 기술1

meeting_list.sort(key=lambda x:(x[1], x[0])) #파이썬의 엄청난 기술2 1차적으로 y성분으로 정렬하고 그 다음에 x 성분으로 정렬한다. 
temp = meeting_list[0][1]
for i in range(1,meeting):
    if meeting_list[i][0] >= temp:
        count += 1
        temp = meeting_list[i][1]
print(count)

