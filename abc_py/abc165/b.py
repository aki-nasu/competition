x = int(input())

ans = 0
money = 100
while True:
    if money >= x: exit(print(ans))
    ans += 1
    money = (money*1.01) // 1