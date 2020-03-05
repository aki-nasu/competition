def F(x):
    return x//2 if x%2==0 else 3*x+1

a = list()
a.append(int(input()))
while True:
    x = F(a[-1])
    if x in a:
        print(len(a)+1)
        exit(0)
    a.append(x)