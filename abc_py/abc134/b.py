# 2019/12/07 60+[m] 2WA
# 難しかった。ACにしたのはいいがこれが適切だとは思えない。
# Nを2Dで割った切り上げが答え。
# 整数のA/Bの切り上げは、(A+B-1)/Bの商と同じ。
n,d = map(int,input().split())
ans = 1
a = d+1
if a+d >= n:
    print(ans)
    exit(0)
while(True):
    a += (2*d)+1
    if a > n:
        if a-d-1<n:
            ans+=1
        print(ans)
        exit(0)
    ans+=1