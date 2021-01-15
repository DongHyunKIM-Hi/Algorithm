
a = []
num = input()
for i in str(num):
    a.append(int(i))
a.sort(reverse=True)
for index in a:
    print(index,end='')