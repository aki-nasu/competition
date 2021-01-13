# s = input()
# if s[-1] == 's':
#     print(s + 'es')
# else:
#     print(s + 's')

# n = int(input())
# cnt = 0
# zoro = False
# for i in range(n):
#     d1,d2 = map(int,input().split())
#     if d1 == d2:
#         cnt += 1
#     else:
#         cnt = 0
#     if cnt == 3:
#         zoro = True
# if zoro:
#     print('Yes')
# else:
#     print('No')

import math

n = int(input())
t = int(math.sqrt(n)) + 1

count = 0
p = 0
for a in range(1,t):
    for b in range(a,1000000):
        if a*b < n:
            count += 1
        else:
            break
        if a==b: p+=1
count = (count*2) - p
print(count)