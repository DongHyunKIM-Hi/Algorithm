#백의 자리 a
#십의 자리 b
#일의 자리 c
#n은 
n = int(input())

for i in range(1,n+1):
    num_sum = list(map(int,str(i)))
    sum_total = i + sum(num_sum)
    want = 0
    if sum_total == n:
        want = i
        break
print(want)