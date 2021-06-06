# 各行・各列の合計値を配列でもたせる
# 各要素ごとに各行・各列の合計値を加算し、自身の値を減算する

h,w = map(int,input().split())
# 各行・各列の合計値を配列でもたせる
ws = [0]*w

import numpy as np
# カラの二次元配列を作成（初期値n, 行row, 列column）
row = h
column = w
n = 0
ans = np.full((row,column),n) 

for i in range(h):
    l = list(map(int,input().split()))
    for j in range(w):
        ans[i][j] += sum(l) - l[j]
        ws[j] += l[j]

# 各要素ごとに各行・各列の合計値を加算し、自身の値を減算する
for i in range(h):
    ans[i] += ws
    print(*ans[i])