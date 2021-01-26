num = int(input())
tmp = [int(input()) for _ in range(num)]
tmp.sort()
sat = 0

for index in range(num):
    unsat = tmp[index] - index -1
    sat += abs(unsat)
print(sat)