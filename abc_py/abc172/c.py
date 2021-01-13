n,m,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.reverse()
B.reverse()

AB = [0]*(len(A)+len(B))
for i in range(len(AB)):
    a = OVER if i < 0 else A[i]
    b = OVER if j < 0 else B[j]
    if a <= b:
        i-=1
    else:
        j-=1



# i,j=len(A)-1,len(B)-1
# count=0
# OVER = pow(10,9)+1
# while True:
#     print(count)
#     print(k)
#     if k < 0:
#         break
#     else:
#         count+=1
# print(count)
