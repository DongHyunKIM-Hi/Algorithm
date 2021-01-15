"""
처음 내  풀이
num = int(input())
test=[int(input()) for _ in range(num)]
result = list(set(test))
result.sort()
for a in result:
    print(a) 
"""

'''
버블 정렬
num = int(input())
test=[int(input()) for _ in range(num)]
for index in range(len(test)-1):
    sort = False
    for index2 in range(len(test)-1-index):
        if test[index2] > test[index2+1]:
            sort = True
            test[index2], test[index2+1] = test[index2+1], test[index2]
    if sort == False:
        break
for a in test:
    print(a)
'''
