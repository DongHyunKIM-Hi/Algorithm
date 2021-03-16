a,b,c = map(int, input().split())
num_list = {}
for index in range(a):
    num_list[index+1] = []

for index in range(b):
    n,m = map(int,input().split())
    num_list[n].append(m)
    num_list[m].append(n)


def DFS(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            graph[node].sort(reverse=True)
            
            need_visit.extend(graph[node])

    

def BFS(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    while need_visit:
        node= need_visit.pop(0)

        if node not in visited:
            visited.append(node)
            print(node, end=' ')
            need_visit.extend(graph[node])
    



DFS(num_list,c)
for index in num_list:
    num_list[index].sort()
print()
BFS(num_list,c)