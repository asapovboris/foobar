def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


staircases = 0
A = 5
lst = list(reversed(range(1, A+1)))

for i in powerSet(lst):
    if len(i) > 1 and sum(i) == A:
        # print (i)
        staircases = staircases + 1

print staircases