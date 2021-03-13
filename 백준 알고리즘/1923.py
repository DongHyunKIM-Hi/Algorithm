cnt = int(input())
num_list=[]
for index in range(cnt):
    num_list.append(list(map(int,input().split())))
count =0
for index in range(1,cnt):
    count = 0
    for index2 in range(len(num_list[index])):
        if index2 == 0:
            num_list[index][0] = num_list[index][0] + num_list[index-1][0]
        elif index2 == len(num_list[index]) -1:
            num_list[index][-1] = num_list[index][-1] + num_list[index-1][-1]
        else:
            num_list[index][index2] = max(num_list[index-1][index2-1], num_list[index-1][index2]) + num_list[index][index2]

print(max(num_list[cnt-1]))