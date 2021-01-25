num,value = map(int,input().split())
coin_list = [int(input()) for _ in range(num)]
coin_count=0
coin_list.sort(reverse=True)
for coin in coin_list:
    count = value // coin
    value -= count * coin
    coin_count += count
print(coin_count)
    