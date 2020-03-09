s = input()
if len(s)%2==0:
    t = 'hi' * (len(s)//2)
    if s == t:
        print('Yes')
        exit(0)
print('No')