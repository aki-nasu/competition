N = int(input())
A = list(map(int,input().split()))
ans = 0
while True:
    for i in range(N):
        if A[i]%2 != 0:
            print(ans)
            exit(0)
        A[i] = A[i]//2
    ans += 1
