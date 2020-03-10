s,x = input(), 1000
for i in range(2,len(s)): x = min(x, abs(753 - int(s[i-2:i+1])))
print(x)