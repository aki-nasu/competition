import itertools
n = int(input())
p = tuple(map(int,input().split()))
q = tuple(map(int,input().split()))
t = list(itertools.permutations(range(1,n+1)))
print(abs(t.index(p) - t.index(q)))
