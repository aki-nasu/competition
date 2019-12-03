N = int(input())
S = input()
ans = ""
for c in S :
    a = ord(c) - ord('A')
    a += N
    a %= 26
    ans += chr(ord('A') + a)
print(ans)