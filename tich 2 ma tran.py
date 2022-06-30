a = [[0, 0, 0],
    [0, 1, 2],
    [0, 5, 6]]

b = [[-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]]
tong = 0
for i in range(3):
    for j in range(3):
        tong += a[i][j]*b[i][j]
print(tong)