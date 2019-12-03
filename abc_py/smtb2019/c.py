x = int(input())
c = x // 100
if 100*c <= x and x <= 105*c:
    print(1)
    exit(0)
print(0)