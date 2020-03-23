n = int(input())
a = []
a.append(int(input()))
# a = int(input())
def F(n,a,j,t):
    if n == 0:
        return t
    else:
        b = a%(pow(10,n))
        k = b//pow(10,n-1)
        t += abs(j-k)*pow(10,n-1)
        return F(n-1,b,k,t)
for i in range(n-1):
    a.append(F(n-1,a[i],a[i]//(pow(10,n-1)),0))
    n-=1
print(a[-1])

# print(x[n-1][0])
# print(x)
