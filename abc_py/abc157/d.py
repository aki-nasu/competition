class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y: return False
        if self.parents[x] > self.parents[y]: x,y = y,x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True
    
    # 根が同じか？
    def same(self, x , y):
        return self.find(x) == self.find(y)

    # 属するUnionの要素数
    def size(self, x):
        return -self.parents[self.find(x)]

n,m,k = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(m)]
cd = [list(map(int,input().split())) for _ in range(k)]

# 初期化
uf = UnionFind(n)
# くっつける
for a,b in ab: uf.unite(a-1,b-1)

# 自身を引く(-1)
ans = [uf.size(i)-1 for i in range(n)]

for a,b in ab:
    if uf.same(a-1,b-1):
        ans[a-1] -= 1
        ans[b-1] -= 1
for c,d in cd:
    if uf.same(c-1,d-1):
        ans[c-1] -= 1
        ans[d-1] -= 1
print(*ans)