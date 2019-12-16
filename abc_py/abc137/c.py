# C - Green Bin
# https://atcoder.jp/contests/abc137/tasks/abc137_c
# 考えはあっているが、実装ができなかった。。
# collectionsライブラリを使った。
# str.joinを使った
# sum(x*(x-1)//2)の部分がまだよくわかっていない

# 15:20 -16:08 giveup
# 21:45 -22:33 review
from collections import Counter

# 3
# acornistnt
# peanutbomb
# constraint
n = int(input())
s = [''.join(sorted(input())) for _ in range(n)]
# s is ['acinnorstt', 'abbemnoptu', 'acinnorstt']
counter = Counter(s)
# counter is Counter({'acinnorstt': 2, 'abbemnoptu': 1})
# counter.values() is dict_values([3, 2])
ans = sum(x*(x-1)//2 for x in counter.values())
print(ans)