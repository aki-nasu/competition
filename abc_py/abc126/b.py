# 15:35 giveup
# パターンを網羅して考えられていなかったため、実装が変になった。
def P(s):
    print(s)
    exit(0)

s = input()
l = int(s[:2])
r = int(s[2:])
if 1 <= l and l <= 12:
    if 1 <= r and r <= 12:
        P("AMBIGUOUS")
    else:
        P("MMYY")
else:
    if 1 <= r and r <= 12:
        P("YYMM")
    else:
        P("NA")