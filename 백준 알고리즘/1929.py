#1929
import math

def test(num):
    if num == 1: return False
    
    n = int(math.sqrt(num))
    
    for index in range(2,n+1):
        if num % index == 0: return False
    return True
a,b = map(int,input().split())

for tmp in range(a,b+1):
    if test(tmp): print(tmp)