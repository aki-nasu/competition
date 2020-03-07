n = int(input())
a = list(map(int,input().split()))
a.sort()
s = list(set(a))
s.sort()
if a == s:
    print('YES')
else:
    print('NO')