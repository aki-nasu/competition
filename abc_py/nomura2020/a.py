h1,m1,h2,m2,k = map(int,input().split())
h=(h2-h1)*60
m=m2-m1
print(h+m-k)