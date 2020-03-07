class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
    def find(self, x):
        if self.parents[x] < 0: return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def unite(self, x, y):
        x,y = self.find(x),self.find(y)
        if x == y: return False
        if self.parents[x] > self.parents[y]: x,y = y,x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True
    def same(self, x, y):
        return self.find(x) == self.find(y)

n,q = map(int,input().split())
uf = UnionFind(n)
ans = list()
for i in range(q):
    p,a,b = map(int,input().split())
    if p == 0:
        uf.unite(a, b)
    else:
        if uf.same(a, b):
            ans.append('Yes')
        else:
            ans.append('No')
for i in range(len(ans)):
    print(ans[i])