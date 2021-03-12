def test(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
    return primes

tmp = 1

while True:
    tmp = int(input())
    if tmp == 0:
        break
    n_2 = set(test(tmp+tmp))
    n_1 = set(test(tmp))
    result = list(n_2 - n_1)
    print(len(result))
    