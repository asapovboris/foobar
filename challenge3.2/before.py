def partitions(n):
    parts = [1] + [0] * n
    for t in range(1, n + 1):
        for i, x in enumerate(range(t, n + 1)):
            # print i, x
            # print parts[x], parts[i]
            parts[x] += parts[i]
            # print parts[n]
    return parts[n]

n = 200
staircases = [1]+[0]* n

for i in range(1, n + 1):
    for j in range(n, i-1, -1):
        staircases[j] += staircases[j - i]

print staircases[n] - 1