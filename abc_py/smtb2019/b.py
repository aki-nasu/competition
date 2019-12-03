import math
n1 = int(input())
n =  n1 * 100
x1 = (n // 108)
x2 = -(-n // 108)
if x1*108//100 == n1:
    print(x1)
    exit(0)
if x2*108//100 == n1:
    print(x2)
    exit(0)
print(":(")