# 22:27-22:40 13[m]
# すぐに方向性決められたので簡単めだったと思う。
k,x = map(int,input().split())

x_min = -1000000
x_max = 1000000

a_min = x - k + 1
a_max = x + k - 1
if a_min < x_min:
    a_min = x_min
    a_max = x_min + k - 1
if a_max > x_max:
    a_max = x_max
    a_min = x_max - k + 1
ans = str(a_min)
t = 0
while(t != (a_max - a_min)):
    t += 1
    ans += " " + str(a_min+t)

print(ans)