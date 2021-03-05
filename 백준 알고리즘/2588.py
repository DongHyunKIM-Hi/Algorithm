a = int(input())
b = input()

for index in range(len(b)-1,-1,-1):
    print(a * int(b[index]))
print(a*int(b))
