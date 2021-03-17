import sys
input= sys.stdin.readline
from collections import Counter
cnt = int(input())
num_list=[]
for index in range(cnt):
    num_list.append(int(input()))

def avg(num_list):
    return round(sum(num_list)/cnt)

def center(num_list):
    num_list.sort()
    return num_list[cnt//2] 

def bindo(num_list):
    tmp = Counter(num_list).most_common()
    if len(num_list) > 1:
        if tmp[0][1] == tmp[1][1]:
            print(tmp[1][0])
        else:
            print(tmp[0][0])
    else:
        print(num_list[0])
    
    

def rang(num_list):
    a = max(num_list)
    b = min(num_list)
    return a-b

print(avg(num_list))
print(center(num_list))
bindo(num_list)
print(rang(num_list))
