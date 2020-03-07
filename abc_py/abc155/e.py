import math
n = int(input())
try:
    t = int(math.log10(n) + 1)
except ValueError:
    t = len(str(n))

count = 0
while True:
    bottom = 10 ** (t-1)
    top = 10 ** t
    
    n = min(top-n,n-bottom)
    try:
        t = int(math.log10(n)+1)
    except ValueError:
        t = len(str(n))
    count += 1
    if n == 0:
        print(count)
        exit(0)