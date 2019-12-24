# 21:09
a,b = map(int,input().split())
import fractions
lcm = a*b // fractions.gcd(a,b)
print(lcm)