def solve( n,x,y):
    global resultif 
    if n==2:
        if x==X and y==Y:
            print(result)
            return
        result += 1
        if x==X and y+1==Y:
            print(result)
            return
        result +=1

        if x+1==X and y==Y:
            print(result)
            return
        result +=1

        if x+1==X and y+1 ==Y:
            print(result)
            return
        result +=1
        return
    solve(n/2,x,y)
    sol