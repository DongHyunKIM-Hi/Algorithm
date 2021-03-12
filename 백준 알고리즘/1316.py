num = int(input())
count = 0
for _ in range(num):
    result = True
    text = input()
    text_test = list(set(text))
    [hyap]
    for index in text_test:
        standard = text.count(index)
        for i in range(1,standard):
            if text[text.index(index)] != text[text.index(index)+i]:
                result = False
    if result:
        count +=1
print(count)

