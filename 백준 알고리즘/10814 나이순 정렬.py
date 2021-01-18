import sys
num = int(sys.stdin.readline())
list_word = []
for index in range(num):
    list_word.append(list(sys.stdin.readline().split()))
list_word.sort(key = lambda x : int(x[0]))
for index in list_word:
    print(index[0], index[1])