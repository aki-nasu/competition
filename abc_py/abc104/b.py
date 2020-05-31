s = input()
if s[0]=='A' and 'C' in s[2:-1]:
    s = s.replace('A','',1).replace('C','',1)
    if s == s.lower():
        exit(print('AC'))
print('WA')