amount=0
n = int(input())
for _ in range(n):
    x,u = input().split()
    x = float(x)
    if u == 'BTC':
        x *= 380000
    amount += x
print(amount)