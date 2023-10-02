length = int(input())
array_list = list(map(int,input().split()))
max_num = array_list[0]
min_num = array_list[0]

for i in range(len(array_list)):
    if array_list[i] > max_num:
        max_num = array_list[i]
    
    if array_list[i] < min_num:
        min_num = array_list[i]
print(min_num,max_num)