s = input()
l = []
for i in range(len(s)):
    l.append(s[i])
print('Yes' if 'abc'==''.join(sorted(l)) else 'No')