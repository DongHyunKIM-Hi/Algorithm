
# result=[]
# cnt = int(input())
# color_list=[[0,0,0] for _ in range(cnt)]
# for index in range(cnt):
#     color_list[index] = list(map(int,input().split()))
#     if index == 0:
#         small = min(color_list[index][0],color_list[index][1],color_list[index][2])
#         result.append(small)
       
#     else:
#         loc = color_list[index-1].index(small)
#         color_list[index][loc] = 999999999
#         small = min(color_list[index])
#         result.append(small)
# print(color_list)    
# print(sum(result))



#########################################
cnt = int(input())

color_list = []

for index in range(cnt):
    colors = list(map(int,input().split()))
    color_list.append(colors)

for index in range(1,cnt):
        color_list[index][0] = min(color_list[index-1][1] , color_list[index-1][2]) + color_list[index][0]
        color_list[index][1] = min(color_list[index-1][0] , color_list[index-1][2]) + color_list[index][1]
        color_list[index][2] = min(color_list[index-1][0] , color_list[index-1][1]) + color_list[index][2]

print(min(color_list[cnt-1]))

