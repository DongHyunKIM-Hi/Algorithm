from collections import deque
n = int(input())
n_list = deque([ index+1 for index in range(n)])


while not(len(n_list)==1):
    n_list.popleft()
    n_list.append(n_list.popleft())


print(n_list[0])