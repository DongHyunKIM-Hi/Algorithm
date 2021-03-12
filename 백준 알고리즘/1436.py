num = int(input())
count =0
start = 666
while not(num == count):
    if str(start).find('666') != -1:
        count += 1
    start += 1
    
print(start-1)