equation = input().split('-')
answer = 0 

for i in equation[0].split('+'):
    answer += int(i)

for j in equation[1:]:
    for k in j.split('+'):
        answer -=  int(k)
print(answer)