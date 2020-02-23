n = int(input())
s = [""]*n
t = [0]*n
for i in range(n):
    l = list(input().split())
    s[i] = l[0]
    t[i] = int(l[1])
x = input()
time_count = 0
for i in range(n):
    time_count += t[i]
    if s[i] == x:
        break
print(sum(t) - time_count)