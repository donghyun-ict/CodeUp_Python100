n = int(input())
l = [[0 for j in range(20)] for i in range(20)]


for i in range(n):
    x, y = map(int, input().split())
    l[x][y] = 1

for i in range(1,20):
    for j in range(1,20):
        print(l[i][j], end=' ')
    print()