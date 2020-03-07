n = int(input())
ans = 'Bad'
if n == 100:
    ans = 'Perfect'
elif 90 <= n:
    ans = 'Great'
elif 60 <= n:
    ans = 'Good'
print(ans)
