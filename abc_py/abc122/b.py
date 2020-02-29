s = input()

count = 0
for i in range(len(s)):
    c=0
    if s[i]!='A' and s[i]!='C' and s[i]!='G' and s[i]!='T':
        continue
    c=1
    for j in range(i+1,len(s)):
        if s[j]!='A' and s[j]!='C' and s[j]!='G' and s[j]!='T':
            break
        else:
            c+=1
    count = c if count<=c else count
print(count)