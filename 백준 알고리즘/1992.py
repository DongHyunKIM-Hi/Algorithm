cnt = int(input())
num_list = []
for index in range(cnt):
    num_list.append(list(input()))
blue = []
white = []
def paper(num_list,blue,white):
    test_blue = []
    test_white = []
    length = len(num_list)
    new_list = []
    for index in num_list:
        if index.count('1') == length:
            test_blue.append(1)
        elif index.count('0') == length:
            test_white.append(1)
        else:
            break

    if len(test_blue) == length:
     
        return blue.append(1)
    elif len(test_white) == length:
    
        return blue.append(0)
    new_list.append([index[0:length//2] for index in num_list[0:length//2]])
    new_list.append([index[length//2:] for index in num_list[0:length//2]])
    new_list.append([index[0:length//2] for index in num_list[length//2:]])
    new_list.append([index[length//2:] for index in num_list[length//2:]])
    blue.append('(')
    return paper(new_list[0],blue,white), paper(new_list[1],blue,white), paper(new_list[2],blue,white), paper(new_list[3],blue,white), blue.append(')')

paper(num_list,blue,white)
for index in blue:
    print(index, end='')

