# s = input()
s = '14282668646'
n = len(s)
if n<4:
    print(0)
    exit(0)
count = 0

for i in range(n):
    if n-i<4:break
    for j in range(3,n-i):
        if i!=0:
            num = int(s[-j-1-i:-i])
        else:
            num = int(s[-j-1:])
        if num%2019==0:print(num)
print(count)