num = int(input())
test = list()
for index in range(num):
    temp = int(input())
    test.append(temp)

def qsort(data):
    if len(data) <= 1:
        return data
    middle = data[0]
    left = [index for index in data if middle > index]
    right = [index for index in data if middle < index]
    return qsort(left) + [middle] + qsort(right) 

qsort(test)