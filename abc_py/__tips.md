# Tips

## ToC
* 入出力
* 文字、文字列
* 順列
* 配列

## 入出力
### 入力
```python
s = input()         # 入力内容を文字列として変数に詰める
n = int(input())    # 入力内容を数値として変数に詰める

# 入力内容を数値として、且つスペース区切りで別々の変数に詰める
n,k = map(int,input().split())      # >>1 3 のような入力
# 別々の変数ではなく、リストとして詰める
l = list(map(int,input().split()))
```

### 出力
```python
print('output')     # オーソドックスな出力処理
# 数値を出力する場合、str()で文字列にする
print(str(3) + " " + str(6))    # 3 6 と出力される
```

## 文字、文字列

### ASCIIコード

* 文字、ASCIIコード間の変換
```python
ord('a')    #97
chr(97)     #'a'
```

#### A to Z . N個ずらすと何になるか？系に使用する。
```python
for c in S :
    a = ord(c) - ord('A')
    a += N
    a %= 26
    ans += chr(ord('A') + a)
print(ans)
```

### 文字の反転
```python
s = 'abcde'
s[::-1]
print(s)
# 'edcba'
```



## 順列

### ビットパターン創出
直積を求める
```python
import itertools
n = 3
status = [(0, 1) for _ in range(n)]
list(itertools.product(*status))
#[(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
```
[参考](https://penguin-code.com/python-binary-combination/)

## 配列（リスト）

## 配列の先頭に追加、削除をする場合、deque()を使用する


## numpy

### 二次元配列
```python
import numpy as np
# カラの二次元配列を作成（初期値n, 行row, 列column）
row = h
column = w
n = 0
l = np.full((row,column),n) 
```

### 文字列へ出力
#### アスタリスク(`*`) でアンパック

```python
my_list = [1, 2, 3]
print(*my_list)
# 出力
# 1 2 3
```

参考： https://qiita.com/LouiS0616/items/1bbe0a9bb93054f6c380

### 繰り返し二乗法

### フェルマーの小定理
#### Links
- [フェルマーの小定理と使い方(Qiita)](https://qiita.com/drken/items/6b4031ccbb2cab7436f3)
- [整数論テクニック集](http://kirika-comp.hatenablog.com/entry/2018/03/12/210446)
- abc156-D
### 逆元
#### Links
- [1000000007で割ったあまりの求め方を総特集（Qiita）](https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a)
- [整数論テクニック集](http://kirika-comp.hatenablog.com/entry/2018/03/12/210446)
- abc156-D









## 以下、未整理。


### 順番を考慮しない2要素の選び方を全探索する
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


# task memo
## スニペット
- inputスニペットからintのみは削除。他、変数は変えられるようにする
