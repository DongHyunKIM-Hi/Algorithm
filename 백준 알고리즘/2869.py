#2869
import sys, math
a,b,c = map(int, sys.stdin.readline().split())
#낮에 올라가는거  a
#밤에 내려가는거 b 
#총 높이 c
day= (c-b) / (a-b)
print(math.ceil(day))