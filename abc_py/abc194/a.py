a,b = map(int,input().split())
if (a+b) >= 15 and b >= 8:
    exit(print(1))
elif (a+b) >= 10 and b >= 3:
    exit(print(2))
elif (a+b) >= 3:
    exit(print(3))
else:
    exit(print(4))
