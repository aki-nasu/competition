def ten2k(n,k):
    if (int(n/k)):
        return ten2k(int(n/k), k) + str(n%k)
    return str(n%k)

n,k = map(int,input().split())
print(len(ten2k(n,k)))