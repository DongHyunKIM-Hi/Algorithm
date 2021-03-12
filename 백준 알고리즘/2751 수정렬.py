num = int(input())
test=[int(input()) for _ in range(num)]
result = list(set(test))

for a in result:
    print(a) 