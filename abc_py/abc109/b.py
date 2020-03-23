n = int(input())
wl = []
wl.append(input())
ans = 'Yes'
for _ in range(1,n):
    w = input()
    if w in wl or wl[-1][-1] != w[0] or ans == 'No':
        ans = 'No'
    else:
        wl.append(w)
print(ans)