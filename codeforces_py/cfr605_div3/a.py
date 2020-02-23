# https://codeforces.com/contest/1272/problem/A
# A. Three Friends
# wakawranai...

q = int(input())
ans = []
for i in range(q):
    a,b,c = sorted(map(int,input().split()))
    # ans.append((min(total)))

for i in range(q):
    print(ans[i])