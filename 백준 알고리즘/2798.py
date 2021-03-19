n,m = map(int,input().split())

num_list  = list(map(int,input().split()))
num_list.sort()
max = 0
for index1 in range(len(num_list)-2):
    for index2 in range(index1+1,len(num_list)-1):
        for index3 in range(index2+1, len(num_list)):
            tmp = num_list[index1] + num_list[index2] + num_list[index3]
            if tmp > max and tmp <= m:
                max = tmp

print(max)