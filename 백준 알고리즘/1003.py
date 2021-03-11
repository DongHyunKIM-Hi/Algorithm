def fibo_dp(num):
    if num == 0:
        return print(1,0)
    elif num == 1:
        return print(0,1)
    cache = [[0 for index in range(num+1)] for index in range(num+1)]
    cache[0][0] = 0
    cache[1][0] = 1
    #값 구하기
    cache[0][1] = 1
    cache[1][1] = 1
    #함수 실행 횟수 구하기
    for index in range(2,num+1):
        cache[index][0] = cache[index-1][0] + cache[index-2][0]
        cache[index][1] = cache[index-1][1] + cache[index-2][1]
    return print(cache[num][1]-cache[num][0], cache[num][0] )

count = int(input())
for _ in range(count):
    num = int(input())
    fibo_dp(num)