a = int(input())
b = int(input())
c = 2
if a == 1:
    if b == 2:
        c = 3
elif a == 2:
    if b == 1:
        c = 3
    else:
        c = 1
elif a == 3:
    if b == 2:
        c = 1
print(c)
