import sys

num= int(sys.stdin.readline())

for index in range(num):
    text = sys.stdin.readline()
    text_left= []
    test =True
    for text_index in text:
        if text_index == "(":
            text_left.append('(')
        elif text_index == ")":
            if text_left:
                text_left.pop()
            else:
                test = False 
    if text_left:
        test=False
    if test:
        print('YES')
    else:
        print('NO')
