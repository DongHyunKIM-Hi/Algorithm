import sys 
num = int(sys.stdin.readline())
def fibo(num):
    if num<=1:
        return num
    return fibo(num-1) + fibo(num-2)
print(fibo(num))