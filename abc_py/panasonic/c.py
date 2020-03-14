a,b,c = map(int,input().split())
print('Yes' if 4*a*b < pow(c-a-b,2) and c-a-b > 0 else 'No')