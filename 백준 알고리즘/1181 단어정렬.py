num = int(input())
list_word = []
for index in range(num):
    word = str(input())
    list_word.append(word)
list_word = list(set(list_word))
list_word.sort(key = lambda x: (len(x),x))

for index in list_word:
    print(index)