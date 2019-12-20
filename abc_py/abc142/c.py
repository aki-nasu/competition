# C - Go to School
# https://atcoder.jp/contests/abc142/tasks/abc142_c
# ''.join()のリストの中身が文字列でないとエラーになったので今回のような書き方になった。
# 簡単だとは思います。


# 23:53 - 00:04 事前にスマホで問題は読んでいる
n = int(input())
a = list(map(int,input().split()))
p = ['0']*n
for i in range(n):
    p[a[i]-1] = str(i+1)
print(' '.join(p))
