num = int(input())

num_list = list(map(int,input().split()))

max_dp = [1 for _ in range(num)]
min_dp = [1 for _ in range(num)]
result = []
for index in range(num):
    for index2 in range(index):
        if num_list[index] > num_list[index2]:
             max_dp[index] = max_dp[index2] +1
    
print(max_dp)
num_list.reverse()

for index in range(num):
    for index2 in range(index):
        if num_list[index] > num_list[index2] and min_dp[index] <= min_dp[index2]:
             min_dp[index] = min_dp[index2] +1
min_dp.reverse()



for index in range(num):
    result.append(max_dp[index] + min_dp[index] -1)

print(max(result))