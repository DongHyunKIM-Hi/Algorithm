case = int(input())

result=[]

for index in range(case):
    get = list(map(int,input().split()))
    avg = sum(get[1:]) / get[0]
    new = list(filter(lambda x : x> avg , get[1:]))
    so = len(new) / len(get[1:]) * 100
    result.append(so)
for index in result:
    print(f'{index:.3f}%')
    