n ,mimport sys
n,m = map(int,sys.stdin.readline().split())

tmp=[]

for _ in range(n):
    tmp.append(sys.stdin.readline())
n_count = 0
m_count = 0

for index in range(n):
    if 'X' not in tmp[index][0:m]:
        n_count += 1

for index in range(m):
    if 'X' not in tmp[0:n][index]:
        m_count += 1

print(n_count if n_count >= m_count else m_count)
        