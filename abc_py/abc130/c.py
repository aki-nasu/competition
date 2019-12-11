# 22:54-23:26 timeup
w,h,x,y = map(int,input().split())
print(str((w*h)/2) + " " + str(1 if x+x == w and y+y == h else 0))