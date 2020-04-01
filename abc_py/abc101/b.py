n=int(input())
s=0
nt=n
while nt>0:
    s+=nt%10
    nt=nt//10
print('Yes' if n%s==0 else 'No')