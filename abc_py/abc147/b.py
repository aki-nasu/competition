s = input()
l = len(s)
s3 = ""
if l%2 == 0:
    s1=s[:l//2]
    s2=s[l//2:]
else:
    s1=s[:l//2]
    s2=s[l//2+1:]
hug = 0
for i in range(l//2):
    if s1[-i-1] != s2[i]:
        hug += 1
print(hug)