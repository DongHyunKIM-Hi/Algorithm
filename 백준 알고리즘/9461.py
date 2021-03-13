dp= [0 for _ in range(101)]
dp[0] = 1
dp[1] =1
dp[2] =1
dp[3] = 1


cnt= int(input())

def trangle(num):
    if num <= 3:
        return 1

    for index in range(4,num+1):
        dp[index] = dp[index-2] + dp[index-3]
    return dp[num]  

for index in range(cnt):
    num = int(input())
    print(trangle(num))
