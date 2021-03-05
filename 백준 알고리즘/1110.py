one = int(input())
count = 0

a = one
while True:
        a
        first = a//10
        second = a%10
        
        a = str(second) + str((first + second)%10)
        a =  int(a)
        count = count +1
        
        if a == one:
            break
print(count)