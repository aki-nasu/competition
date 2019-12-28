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

### 配列をコピーする
```python
a_sort = copy.deepcopy(a)
```
単純にイコール（a_sort = a）すると、aを参照し続けるため
a_sort.sort()などの操作が、aに及んでしまう。

### 要素の総和
sum(w[:1])　の書き方でリスト内の要素の総和が取れる

pow:累乗、math.sqrt

### 切捨て、切上げ
整数のA/Bの切り上げは、(A+B-1)/Bの商と同じ

```python
# 切り捨て
4 // 3
# 切り上げ
-(-4 // 3)
```

文字をいい感じに回すときに使って。
```python
for c in S :
    a = ord(c) - ord('A')
    a += N
    a %= 26
    ans += chr(ord('A') + a)
print(ans)
```

### リスト内包表記

```python
squares = [i**2 for i in range(5)]
print(squares)
# [0, 1, 4, 9, 16]
```

* 三項演算子とリスト内包表記
```python
odd_even = ['odd' if i % 2 == 1 else 'even' for i in range(10)]
print(odd_even)
# ['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd']
```

## 文字列操作
### join
`デリミタ.join(リスト)`
```python
str_list = ['python', 'list', 'exchange']
mojiretu = ','.join(str_list)
print(mojiretu)
```
```
python,list,exchange
```

#### 文字列をソートしてリストに入れる
```python
# ABC137より
s = [''.join(sorted(input())) for _ in range(n)]
```

## 最大順、最小順で要素を取り出す場合
### priority que / heap que / 優先度キュー
`heapq`を使用する。

```python
import heapq
# リストxをヒープに変換
heapq.heapify(x)
# 最小の要素を取り出す（popする）
heapq.heappop(x)
# 値をpushする
heapq.push(x)

## 最大値を扱う場合は、マイナスする
# 注意：マイナスのまま取り出した要素を計算すると、誤差が生じる（小数点以下の大小が逆転するとか）
# 入力を受け取った時点でマイナスにする
a = list(map(lambda x: -int(x),input().split()))
heapq.heapify(a)
# 計算する際は、取り出した要素を正の整数として計算すること。
for _ in range(m):
    tmp = (-heapq.heappop(a)) // 2
    heapq.heappush(a, -tmp)
print(-sum(a))
```

## 数学的な言葉
### 非負整数
0を含む正の整数のこと
