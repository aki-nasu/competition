a,b,c,d = map(int,input().split())
taka = b/a
aoki = d/c
if taka == aoki:
    print('DRAW')
elif taka > aoki:
    print('TAKAHASHI')
else:
    print('AOKI')