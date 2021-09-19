n = int(input())
a = list(map(int, input().split()))
m = a[0]

for i in range(1, n):
    if (m > a[i]):
        m = a[i]

print(m)