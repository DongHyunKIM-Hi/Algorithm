import sys
num = int(sys.stdin.readline())
test = []

for i in range(num):
    test.append(list(map(int,sys.stdin.readline().split())))

test.sort(key=lambda x:(x[1],x[0]))

for a in test:
    print(a[0] ,a[1]) 

