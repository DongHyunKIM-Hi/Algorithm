num = int(input())

num_list = list(map(int,input().split()))

num_list.sort()

dp = [0 for _ in range(num)]
dp[0] = num_list[0]

for index in range(num):
    if index == 0:
        dp[0] = num_list[0]
    else:
        dp[index] = dp[index - 1] + num_list[index]

print(sum(dp))