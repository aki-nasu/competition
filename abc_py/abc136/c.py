# C - Build Stairs
# https://atcoder.jp/contests/abc136/tasks/abc136_c
# きっと裏があると思いつつ、ACになった。拍子抜け。
# 「単調非減少」となっているか、というのが何を言っているのかはじめ分からなかったが、
# タイトルが階段をつくるとなっていることから一度高さが高くなったら、低くなれないということで理解した。

# 14:53 - 15:09
n = int(input())
h = list(map(int,input().split()))
for i in range(n-1):
    if h[i] > h[i+1]:
        print("No")
        exit(0)
    elif h[i] < h[i+1]:
        h[i+1] = h[i+1] - 1
print("Yes")