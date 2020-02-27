time = 0
d = 10
for _ in range(5):
    a = int(input())
    r = a%10
    if (0<r and r<d) or d==10 or (0<r and d==0):
        d,t = r,a
    time += a//10
    if r!=0: time+=1
time -= t//10
if d!=0: time-=1
time *= 10
time += t
print(time)