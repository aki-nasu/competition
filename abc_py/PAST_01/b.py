n = int(input())
x = int(input())
t = []
for _ in range(1,n):
    a = int(input())
    if a == x:
        t.append('stay')
    elif a > x:
        t.append('up ' + str(a-x))
    else:
        t.append('down ' + str(x-a))
    x = a
for i in range(len(t)):
    print(t[i])
