# D - Powerful Discount Tickets
# https://atcoder.jp/contests/abc141/tasks/abc141_d
# TLEが出てしまい、giveup
# priority-queを使用する

# 12:10 giveup
import heapq
n,m = map(int,input().split())
a = list(map(lambda x: -int(x),input().split()))
heapq.heapify(a)
for _ in range(m):
    tmp = (-heapq.heappop(a)) // 2
    heapq.heappush(a, -tmp)
print(-sum(a))