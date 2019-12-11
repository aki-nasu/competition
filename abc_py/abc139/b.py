# 12/11 15:50 give up
# 高橋くんの家には電源プラグの差込口が1口しかありません。
# 上記のパターンを見落としていた。1口で十分な場合、電源タップは0個で良い。
a,b = map(int,input().split())
ans = 0
t = 1
while True:
    if t >= b:
        print(ans)
        exit(0)
    ans += 1
    t = t-1 + a
