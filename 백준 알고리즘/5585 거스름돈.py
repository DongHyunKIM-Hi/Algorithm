coin_list= [500,100,50,10,5,1]
tmp = int(input())
value = 1000 - tmp
coin_count = 0
for coin in coin_list:
    count = value // coin
    value -= coin * count
    coin_count += count
    
print(coin_count)