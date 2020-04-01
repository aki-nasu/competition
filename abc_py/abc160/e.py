x,y,a,b,c = map(int,input().split())
p = sorted(list(map(int,input().split())),reverse=True)
q = sorted(list(map(int,input().split())),reverse=True)
r = sorted(list(map(int,input().split())),reverse=True)
pr = sorted(p+r,reverse=True)
qr = sorted(q+r,reverse=True)

ans = 0
p_ans = 0
q_ans = 0
if sum(p[:x])>=sum(pr[:x]):
    p_ans = sum(p[:x])
if sum(q[:y])>=sum(qr[:y]):
    q_ans = sum(q[:y])
if p_ans != 0 and q_ans != 0:
    ans = p_ans + q_ans
elif p_ans != 0:
    

print(ans)