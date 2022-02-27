def solution(start, length):
    checksum=0
    for i in range(0, length):
        a = start+(length*i)
        b = start+(length*i)+(length-i)-1
        if a % 2 == 0 :
            var_xor = [b, 1, b+1, 0]
        else:
            var_xor = [a, a^b, a-1, (a-1)^b]
        checksum ^= var_xor[(b - a) % 4]
    return checksum