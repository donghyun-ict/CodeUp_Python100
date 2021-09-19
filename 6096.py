l = [(0 for j in range(19)) for i in range(19)]

for i in range(19):
        l[i] = list(map(int, input().split()))

n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    for j in range(19):
        if (l[x-1][j] == 0):
            l[x-1][j] = 1
        else:
            l[x-1][j] = 0
        if (l[j][y-1] == 0):
            l[j][y-1] = 1
        else:
            l[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(l[i][j], end=' ')
    print()