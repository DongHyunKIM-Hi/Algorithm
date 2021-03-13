
memo = [[[0]*21 for _ in range(21)] for __ in range(21)]


def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        # a,b,c 가 음수거나 영이면 1
        return 1 
    
    if a > 20 or b > 20 or c > 20:
        #a,b,c는 20보다 크면 20으로 줄어준다.
        return w(20,20,20)

    if a < b < c:
        # a<b<c
        if (memo[a][b][c]):
            return memo[a][b][c]
        memo[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return memo[a][b][c]
    else:
        if (memo[a][b][c]):
            return memo[a][b][c]
        memo[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memo[a][b][c]

while True :
 
    a, b, c = map(int, input().split())
 
    if a== -1 and b==-1 and c==-1 :
        break
 
    print("w(%d, %d, %d) = %d"%(a, b, c, w(a, b, c)))
