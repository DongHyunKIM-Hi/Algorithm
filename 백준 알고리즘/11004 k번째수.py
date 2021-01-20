a,b = map(int, input().split())
test = list(map(int,input().split()))
test.sort()
test[b-1]


def mergesplit(data):
    print(data)
    if len(data) <= 1:
        return data
    middle = len(data)//2
    left = mergesplit(data[:middle])
    right = mergesplit(data[middle:])
    return merge(left,right)

def merge(left, right):
    lp,rp = 0,0
    merged=[]
    while len(left) > lp and len(right) > rp:
        if left[lp] > right[rp]:
            merged.append(right[rp])
            rp = rp + 1
        else:
            merged.append(left[lp])
            lp = lp + 1
    while len(left) > lp:
        merged.append(left[lp])
        lp = lp + 1
    while len(right) > rp:
        merged.append(right[rp])
        rp = rp +1
    return merged

print(mergesplit(test))
