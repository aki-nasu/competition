# 22:10
import sys
sys.setrecursionlimit(10 ** 7)
def f(n):
    if n < 2:
        return 1
    else:
        return n * f(n-2)

n = int(input())
ret = f(n)
ans = 0
for i in range(1,len(str(ret))):
    if str(ret)[-i] == "0":
        ans += 1
    else:
        print(ans)
        exit(0)