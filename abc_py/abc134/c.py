# C - Exception Handling
# https://atcoder.jp/contests/abc134/tasks/abc134_c
# なにこれ？ゴミ簡単でした。
# deepcopyを使いました。

# 23:59 - 0:10
import copy
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a_sort = copy.deepcopy(a)
a_sort.sort()
max = a_sort[n-1]
max_next = a_sort[n-2]
for i in range(n):
    if a[i] == max:
        print(max_next)
    else:
        print(max)
