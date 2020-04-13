n,x = map(int,input().split())
count = n
m_min = 1001
for _ in range(n):
    m = int(input())
    x -= m
    m_min = min(m, m_min)
while x >= m_min:
    x -= m_min
    count += 1
print(count)