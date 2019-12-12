# competition
競技プログラミングのローカルコード保存用

# Tips
## 順番を考慮しない2要素の選び方を全探索する
内側のループ変数の始点を外側のループ変数 +1 から始めるといい。
```python
n = int(input())
d = list(map(int,input().split()))
ans = 0
for i in range(n):
    for j in range(i+1,n):
        if i != j:
            ans += d[i] * d[j]
```
ref:[B - TAKOYAKI FESTIVAL 2019](https://atcoder.jp/contests/abc143/tasks/abc143_b)

## 範囲指定がある場合（A<=n<=B）は、F(X)関数をつくって、F(B)-F(A-1)で計算するほうが考えやすい

## 最小公倍数(lcm)と最大公約数(gcd)ならびにユークリッド互除法
ref:[C - Anti-Division](https://atcoder.jp/contests/abc131/tasks/abc131_c)
