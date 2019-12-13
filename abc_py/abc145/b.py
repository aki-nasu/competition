# 2019-11-27 14:55:48
N = int(input())
S = input()
ans = "No"
if N%2 != 1 and S[:N//2] == S[N//2:]:
    ans = "Yes"
print(ans)
