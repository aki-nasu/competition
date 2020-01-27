h = int(input())
x = 0
while True:
    if h < 2**x:
        break
    else:
        x += 1
print(2**x - 1)