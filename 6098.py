house = [[0]*10 for i in range(10)]
for i in range(10):
    house[i] = list(map(int, input().split()))

i = 1
j = 1

while ((house[i][j+1] != 1) or (house[i+1][j] != 1)) and (house[i][j] != 2):
    if (house[i][j+1] == 1):
        house[i][j] = 9
        i += 1
    else:
        house[i][j] = 9
        j += 1

house[i][j] = 9

for i in range(10):
    for j in range(10):
        print(house[i][j], end=' ')
    print()