#2606

total_com = int(input())

pair_num =  int(input())

graph = {}

for index in range(total_com):
    graph[index+1] = []

for _ in range(pair_num):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = -1

def col(graph, start_node,count):
    need_visit, visited = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            count +=1
            need_visit.extend(graph[node])
    return count

print(col(graph,1,count))

