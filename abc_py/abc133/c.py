# 22:28 -23:12 解説などを探りつつ。
# 発想が正しくて実装が間違っていたパターン。もったいない。
# 全探索の計算量はきっと多いだろうから、2019の倍数があれば必ず0になる。
# 2019の倍数が無いということは範囲は2019より小さいので全探索に切り替えて調べるという思考。
l,r = map(int,input().split())
if r-l > 2019:
    print(0)
    exit(0)
m = 2019
for i in range(l,r):
    for j in range(l,r+1):
        if i != j and (i*j)%2019 < m:
            m = (i*j)%2019
print(m)