a,b = map(int,input().split())
ans = a-2*b
ans = 0 if ans < 0 else ans
print(ans)