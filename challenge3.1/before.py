# print 0^1^2^3^4^6
# print 17^18^19^20^21^22^23^25^26^29

id = 17
workers = 4
workers_count = workers + id
checksum = 0
flag = True

for j in range(0, workers):
    print id
    print workers_count
    print len(range(id, workers_count))
    print "----------"

    for i in range(id, workers_count):
        print checksum
        checksum = checksum ^ i
    id = id + workers
    workers_count = id + workers - j - 1
print checksum

# print 20^21^22