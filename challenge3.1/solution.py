def solution(start, length):
    workers_count = length + start
    checksum = 0
    for j in range(0, length):
        for i in range(start, workers_count):
            checksum = checksum ^ i
        start = start + length
        workers_count = start + length - j - 1
    return checksum