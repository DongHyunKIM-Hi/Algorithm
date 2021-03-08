#10250
num = int(input())
result = []
for _ in range(num):
    h,w,n = map(int,input().split())
    room = (n//h)+1
    floor = n%h
    if floor ==  0:
        floor = h
        room -= 1
    result_temp = str(floor) + str(room).zfill(2)
    result.append(result_temp)
for want in result:
    print(want)