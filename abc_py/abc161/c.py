n,k = map(int,input().split())
t = n//k
n = abs(n - (k*t))
while n > 0:
    if n <= abs(n-k):
        print(n)
        exit(0)
    n = abs(n-k)
print(n)