# 15:29 -15:34 5m
# なにこれ？簡単すぎて気持ちが悪い・・。何か特別な意図がある問題？？
r,d,x = map(int,input().split())
for _ in range(10):
    x = (r*x) - d
    print(x)