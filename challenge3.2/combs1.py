def combs(xs, i=0):
    if i==len(xs):
        yield ()
        return
    for c in combs(xs,i+1):
        yield c
        yield c+(xs[i],)

A = 5
lst = list(reversed(range(1, A+1)))

print list(combs(range(A)))