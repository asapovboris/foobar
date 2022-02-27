s = '--->-><-><-->-'

path = list(s)
print path
# print path[3]
# print path[3+1:]

salutes = 0
for i in xrange(len(path)):
    # print i
    if path[i] == '>':
        # print path[i]
        # print path[i+1:].count('<')
        salutes = salutes + path[i+1:].count('<')

print salutes*2