test= list(map(str,input()))
want = list(map(str,input()))
count = 0
tmp = len(test)
index = 0
while tmp > 0:
    
    if test[index:index+len(want)] == want:
        count +=1
        tmp = tmp - len(want)
        index = index + len(want)
    else:
        tmp -= 1
        index += 1
print(count)