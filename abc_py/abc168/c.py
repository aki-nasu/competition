import math
a,b,h,m = map(int,input().split())
ra = h * 30 + m * 0.5
rb = m * 6
r = math.radians(abs(ra-rb))
# (abs(ra-rb)*math.pi)/180
print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(r)))
