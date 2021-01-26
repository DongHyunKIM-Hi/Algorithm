import sys
crain_count = int(sys.stdin.readline())
crain_list = list(map(int,sys.stdin.readline().split()))
box_count = int(sys.stdin.readline())
box_list = list(map(int,sys.stdin.readline().split()))

crain_list.sort(reverse=True)
box_list.sort(reverse=True)

time = 0
if crain_list[0] < box_list[0]:
    print(-1)
    exit()

while True:
    time +=1
    for crain in crain_list:
        
        if not box_list :
            break
        box_list.sort(key= lambda x: x>crain)
        if box_list[0] < crain:
            
            box_list.pop(0)
    if not box_list:
        break
print(time)
   
