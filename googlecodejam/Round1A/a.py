import re
message = []
t = int(input())
for _ in range(t):
    n = int(input())
    P = [input() for _ in range(n)]
    ans = '*'
    for i in range(n):
        flg = True
        s = P[i].replace('*','')
        # print('=======')
        # print(s)
        for j in range(n):
            if P[j][0] == '*':
                check = P[j].replace('*','')
            else:
                check = P[j].replace('*','[A-Z]')
            # print("  " + check)
            if not re.search(check, s):
                flg = False
                break
        # print('=======')
        if flg: ans = s
    message.append(ans)

for i in range(t):
    print('Case #' + str(i+1) + ': ' + message[i])