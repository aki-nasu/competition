k = int(input())
s = input()

if len(s) <= k: exit(print(s))
j = len(s) - k
print(s[:k] + '...')