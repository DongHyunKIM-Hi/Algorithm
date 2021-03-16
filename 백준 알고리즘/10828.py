import sys
num = int(sys.stdin.readline())
stack= []

def push(num):
    stack.append(num)

def pop():
    if len(stack) ==0:
        return print("-1")
    return print(stack.pop())
def size():
    return print(len(stack))
def empty():
    if len(stack) == 0:
        return print('1')
    else:
        return print('0')
def top():
    if len(stack) == 0:
        return print('-1')
    return print(stack[-1])
    


for index in range(num):
    want = list(map(str,sys.stdin.readline().split()))

    if want[0] == "push":
         push(int(want[1]))
    elif want[0] == 'pop':
        pop()
    elif want[0] =='top':
        top()
    elif want[0] =='size':
        size()
    elif want[0] == 'empty':
        empty()

