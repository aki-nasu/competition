h,w = map(int,input().split())
t = (w//2)+(w%2)
print(t*((h+1)//2) + (w-t)*(h//2) if h!=1 and w!=1 else 1)