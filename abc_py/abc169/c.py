a,b = input().split()
a = int(a)
b = b.split('.')
b = int(b[0] + b[1])
print(a * b // 100)
