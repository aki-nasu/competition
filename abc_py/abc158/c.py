a,b = map(int,input().split())
for x in range(max(a,b),10001):
    if (x*0.08)//1 == a and (x*0.1)//1 == b:
        print(x)
        exit(0)
print(-1)
