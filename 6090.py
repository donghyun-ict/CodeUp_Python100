a, m, d, n = map(int, input().split())
r = a 

for i in range(n-1):
    r = r * m + d

print(r)