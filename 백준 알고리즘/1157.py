test = input()
test = test.upper()
temp = list(set(test))
count = []
for index in temp:
    count.append(test.count(index))

if count.count(max(count)) >  1 :
    print('?')
else:
    print(temp[count.index(max(count))])