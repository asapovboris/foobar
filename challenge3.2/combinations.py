N = 4

lst = list(reversed(range(1, N+1)))
print lst
lstCombos = []
for Length in range(0, len(lst)+1):
    for i in lst:
        if not lst[lst.index(i):lst.index(i) + Length] in lstCombos:
            combo = lst[lst.index(i):lst.index(i)+Length]
            if len(combo) > 1:
                lstCombos.append(combo)
                print combo

print lstCombos