# C - Attack Survival
# https://atcoder.jp/contests/abc141/tasks/abc141_c
# 問題文そのまま実装しようとすると、N-1人分の繰り返しが必要になるが、
# 最初から最低点を各自に振って、正解した人だけ足しこめばシンプルになる

# 17:07-17:23
# 椅子から飛び出しそうな我が子をあやしながらでも解けた。
n,k,q = map(int,input().split())
score = [k-q]*n
for i in range(q):
    score[int(input()) - 1] += 1
for i in range(n):
    if score[i] > 0:
        print("Yes")
    else:
        print("No")
