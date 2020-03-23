def F(x):
    return x[0:len(x)//2] == x[::-1][0:len(x)//2]

s = input()
n = len(s)
sf = s[0:(n-1)//2]
sb = s[(n+3)//2-1:]
if F(sf) and F(sb) and F(s):
    print('Yes')
else:
    print('No')