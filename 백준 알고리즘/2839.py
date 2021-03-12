num = int(input())
count = 0
bag_5 = 0
bag_3 = 0
while True:
    if(num%5==0):
        bag_5 = num//5
        num = num - (5 * bag_5)
        break;
    num = num-3
    if num < 0:
        break
    bag_3 +=1

if num == 0 or num == -3:
    print(bag_5+bag_3)
else:
    print(-1)



    