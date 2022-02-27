def partitions(n):
    partitions_of = []
    partitions_of.append([()])
    partitions_of.append([(1,)])
    for num in range(2, n+1):
        ptitions = set()
        for i in range(num):
            for partition in partitions_of[i]:
                # print len(partition)
                # print sum(set(partition))
                ptitions.add(tuple(sorted((num - i, ) + partition)))
        partitions_of.append(list(ptitions))
    return partitions_of[n]

N = 10
staircases = 0
partitions = partitions(N)
# print partitions
for i in partitions:
    if len(i) > 1 and sum(set(i)) == N:
        staircases = staircases + 1

print staircases