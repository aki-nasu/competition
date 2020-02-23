w,h = map(int,input().split())
if(divmod(w,4) == divmod(h,3)):
    print('4:3')
else:
    print('16:9')