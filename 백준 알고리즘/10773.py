num = int(input())
num_list = []
for index in range(num):
    tmp = int(input())
    if tmp:
        num_list.append(tmp)
    else:
        num_list.pop()

print(sum(num_list))