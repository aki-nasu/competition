a,b = input().split()
r_a = ""
r_b = ""
for _ in range(int(b)):
    r_a = r_a + a
for _ in range(int(a)):
    r_b = r_b + b
print(min(r_a,r_b))