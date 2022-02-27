def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

n = 10

answer = []
partitions = partitions(n)
# print partitions
for i in partitions:
    if len(i) > 1 and sum(set(i)) == n:
        staircases = staircases + 1

print staircases