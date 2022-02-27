def solution(s):
    path = list(s)
    salutes = 0
    for i in xrange(len(path)):
        if path[i] == '>':
            salutes = salutes + path[i + 1:].count('<')

    return salutes * 2