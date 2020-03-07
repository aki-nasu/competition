s = input()
try:
    ans = int(s)
    ans = ans*2
except ValueError:
    ans = 'error'
print(ans)

# 他の解答
# s = input()
# if s.isdigit():
#     print(int(s)*2)
# else:
#     print('error')