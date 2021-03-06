num1 = set(range(1,10000))
num2 = set()

for index in num1:
    #index = 24
    #index = 25
    for num in str(index):
        # 만약에 index 24라고하면 이 반복문은 
        # 첫번째 num = 2 두번째 num = 4
        # index = 24 + 2 + 4
        index += int(num)
    num2.add(index)
        #num2 = [num_origin= 30]

self_num = num1 - num2

for this in sorted(self_num):
    print(this)