def Tlqkf(array):
    now = array[0]
    result = 1
    for i in range(1,len(array)):
        if now < array[i]:
            result += 1
            now = array[i]
    return result

num = int(input())
tmp = []
for _ in range(num):
    tmp.append(int(input()))

print(Tlqkf(tmp))
tmp.reverse()
print(Tlqkf(tmp))