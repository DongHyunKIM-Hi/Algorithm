#2805
tree_num, need_high = map(int,input().split())
tree_list= list(map(int,input().split()))
tree_list.sort(reverse=True)
big = tree_list[0]
small = 1
result = 0
while big >= small:
    mid = (big + small)//2
    total = 0
    for tree in tree_list:
        if tree < mid:
            break
        total = total + (tree-mid)
    if total >= need_high:
        result = mid
        small = mid +1
    elif total < need_high:
        big = mid -1

print(result)