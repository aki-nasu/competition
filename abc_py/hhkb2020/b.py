h,w = map(int,input().split())
s = []
count = 0
for _ in range(h):
    p = input()
    s.append(p)
    for i in range(w-1):
        if p[i] == '.' and p[i+1] == '.': count += 1 
for i in range(w):
    for j in range(h-1):
        if s[j][i] == '.' and s[j+1][i] == '.': count += 1
print(count)