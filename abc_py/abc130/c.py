# 22:54-23:26 timeup
w,h,x,y = map(int,input().split())

max_area = w * h

x_area = (w-x) * h
x_min = min(x_area,max_area - x_area)

y_area = (h-x) * w
y_min = min(y_area,max_area - y_area)

ans = str(max(x_min,y_min))
if x_min == y_min:
    ans += " 1"
else:
    ans += " 0"
print(ans)
