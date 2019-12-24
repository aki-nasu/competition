a,b = map(int,input().split())
if 5 >= a:
    b = 0
elif 5 <= a and a <= 12:
    b = b // 2
print(b)