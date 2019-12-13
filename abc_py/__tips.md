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

## リスト系
### カラの配列つくる
p = []
p.append()

あるいは
p = [0]*9
必要な分だけ0埋めする

### 要素の総和
sum(w[:1])　の書き方でリスト内の要素の総和が取れる

pow:累乗、math.sqrt


整数のA/Bの切り上げは、(A+B-1)/Bの商と同じ


文字をいい感じに回すときに使って。
```python
for c in S :
    a = ord(c) - ord('A')
    a += N
    a %= 26
    ans += chr(ord('A') + a)
print(ans)
```