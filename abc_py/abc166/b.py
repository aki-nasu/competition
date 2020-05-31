n,k = map(int,input().split())
snuke = [0]*n
for _ in range(k):
    d = int(input())
    L = list(map(int,input().split()))
    for i in range(d):
        snuke[L[i]-1] += 1
print(snuke.count(0))