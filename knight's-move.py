s = input().split()
n, m = int(s[0]), int(s[1])
desc = []
for i in range(n):
    desc.append([0]*m)
desc[0][0] = 1

for i in range(n):
    for j in range(m):
        if i + 2 < n  and  j + 1 < m:
            desc[i+2][j+1] += desc[i][j]
        if i + 1 < n  and  j + 2 < m:
            desc[i + 1][j + 2] += desc[i][j]
'''for i in range(n):
    print(desc[i])'''
print(desc[n-1][m-1])