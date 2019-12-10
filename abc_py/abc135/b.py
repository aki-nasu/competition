# 40[m]くらい。ただただ実直に解いた感じ。
# 3つ以上違えばアウト、2つ違って入れ替えた結果が違うならアウト
n = int(input())
p = list(map(int,input().split()))
q = list(range(1,n+1))
if p == q:
    print("YES")
    exit(0)
cnt = 0
for i in range(n):
    if p[i] != q[i]:
        cnt += 1
        if cnt == 1:
            t = i
        if cnt == 2:
            if p[t] != q[i]:
                print("NO")
                exit(0)
    if cnt > 2:
        print("NO")
        exit(0)
print("YES")