row = int(input())
dx= [1,-1,0,0] 
dy= [0,0,-1,1]
# 오른쪽 , 왼쪽, 아래 ,위
map_list = []
result=[]
def DFS(x,y):
    need_visited = list()
    need_visited.append([x,y])
    count =0
    while need_visited:
        start = need_visited.pop()
       
        map_list[start[0]][start[1]] = 0

        count +=1

        for index in range(4):
            a = start[0] + dx[index]
            b = start[1] + dy[index]
            test = [a,b]
            if 0 <= a < row and 0 <= b < row and map_list[a][b] == '1':
                need_visited.append([a,b])
                map_list[a][b] = 0
                ok_test = [a,b]   
    result.append(count)  




for index in range(row):
    tmp = list(map(str,input()))
    map_list.append(tmp)

for x in range(row):
    for y in range(row):
        if map_list[x][y] == '1':
            DFS(x,y)

print(len(result))
result.sort()
for index in result:
    print(index)