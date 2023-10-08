n = int(input())
meeting = []
for _ in range(n):
    n1 = map(int,input().split())
    meeting.append(list(n1))
meeting.sort(key=lambda x: (x[1],x[0]))
answer = 0
endtime = 0
for i in range(n):
    if endtime <= meeting[i][0]:
        endtime = meeting[i][1]
        answer += 1

print(answer)

