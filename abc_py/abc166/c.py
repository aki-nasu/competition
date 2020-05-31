n,m = map(int,input().split())
judge = [1]*n
H = list(map(int,input().split()))

for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    if H[a] > H[b]:
        judge[b] *= 0
    elif H[a] < H[b]:
        judge[a] *= 0
    else:
        judge[a] *= 0
        judge[b] *= 0
print(sum(judge))