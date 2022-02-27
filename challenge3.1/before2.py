def xor(a, b):
    print a , b
    if(a%2==0):
        xor_rotation = [b, 1, b+1, 0]
    else:
        xor_rotation= [a, a^b, a-1, (a-1)^b]
    print xor_rotation[(b-a)%4]
    return xor_rotation[(b-a)%4]

def answer(start, length):
    checksum=0
    for i in range(0, length):
        a = start+(length*i)
        b = start+(length*i)+(length-i)-1
        if a % 2 == 0 :
            var_xor = [b, 1, b+1, 0]
        else:
            var_xor = [a, a^b, a-1, (a-1)^b]
        checksum ^= var_xor[(b - a) % 4]
        print '-'
    return checksum

print answer(17, 4)