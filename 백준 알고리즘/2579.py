cnt = int(input())
stair = [0 for _ in range(cnt)]
dp=[ 0 for _ in range(cnt)]
for index in range(cnt):
    stair[index] = int(input())
dp[0] = stair[0] # 계단 1의 최대값
if(cnt > 1):
    dp[1] = dp[0] + stair[1] # 계단 2의 최대값

def max_stair(n):
    if (n < 2):
        return dp[n]
    if dp[n]:
        return dp[n]
    dp[n] = max(max_stair(n-2), max_stair(n-3) + stair[n-1]) + stair[n]
    return dp[n] 

print(max_stair(cnt-1))

