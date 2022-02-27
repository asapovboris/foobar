def solution(n):
    staircases = 0
    partitions_of = []
    partitions_of.append([()])
    partitions_of.append([(1,)])
    for num in range(2, n + 1):
        ptitions = set()
        for i in range(num):
            for partition in partitions_of[i]:
                ptitions.add(tuple(sorted((num - i,) + partition)))
        partitions_of.append(list(ptitions))
    partitions = partitions_of[n]
    for i in partitions:
        if len(i) > 1 and sum(set(i)) == n:
            staircases = staircases + 1
    return staircases