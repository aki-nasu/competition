n,m,x = map(int,input().split())
CA = [tuple(map(int,input().split())) for _ in range(n)]
CA = sorted(CA, key=lambda x: x[0])
print(CA[0:2])
# ans = pow(10,5)+1
# for a in range(n):
#     ca = CA[a]
#     if ca[1] >= x and ca[2] >= x and ca[3] >= x: ans = min(ans,ca[0])
# if ans < pow(10,5)+1: exit(print(ans))
# for a in range(n):
#     ca = CA[a]
#     for c in range(1,n-1):
#         ca = 