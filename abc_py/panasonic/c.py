import math
a,b,c = map(int,input().split())
print('Yes' if 2*math.sqrt(a*b) < c-a-b else 'No')