a,b = map(int,input().split())
dist = abs(a-b)
if dist % 2 != 0:
    print("IMPOSSIBLE")
    exit(0)
if a >= b:
    print(a - (dist//2))
else:
    print(a + (dist//2))