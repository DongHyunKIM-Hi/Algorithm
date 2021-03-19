import sys
input= sys.stdin.readline

n= int(input())
n_list = list(map(int,input().split()))
n_list.sort()
m= int(input())
m_list = list(map(int,input().split()))



def binary_search(n_list,want):
    if len(n_list) == 0:
        return False
    if len(n_list) ==1 and n_list[0] == want:
        return True
    if len(n_list) == 1 and n_list[0] != want:
        return False
    
    middle = len(n_list)//2

    if n_list[middle] > want:
        return binary_search(n_list[:middle], want)
    if n_list[middle] < want:
        return binary_search(n_list[middle:], want)
    if n_list[middle] == want:
        return True

for index in m_list:
    if binary_search(n_list,index):
        print(1)
    else:
        print(0)
    

    