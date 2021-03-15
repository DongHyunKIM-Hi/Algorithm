init = input()

test = init.split('-')

result = []

for index in test:
    value = index
    value = value.split('+')
    value = list(map(int,value))
    value = sum(value)        
    result.append(value)
total = result[0]
for index in range(1,len(result)):
    total = total - result[index]

print(total)
