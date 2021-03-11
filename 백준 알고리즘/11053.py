n = int(input())
num_list = list(map(int,input().split()))
dp = [0 for i in range(n)]
for center in range(n):
    for move  in range(center):
        if num_list[center] > num_list[move] and dp[center] <dp[move] :
            dp[center] = dp[move]
    dp[center] +=1
print(max(dp))
