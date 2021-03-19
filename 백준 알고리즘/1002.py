cnt = int(input())

for index in  range(cnt):
    test = list(map(int,input().split()))
    rand = test[2] + test[5]
    length = ((test[0] - test[3])**2 + (test[1] - test[4])**2)**.05
    if length == 0:
        if test[2] == test[5]:
            print(-1)
        else:
            print(0)

    else:

        if length == rand or length == abs(test[2] - test[5]):
            print(1)
        
        elif length < rand and length > abs(test[2] - test[5]):
            print(2)
        else:
            print(0)
