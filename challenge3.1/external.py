def xor(a, b):
    if(a%2==0):
        xor_rotation = [b, 1, b+1, 0]
    else:
        xor_rotation= [a, a^b, a-1, (a-1)^b]
    return xor_rotation[(b-a)%4]

def answer(start, length):
    res=0
    for i in range(0, length):
        # print i
        # print start+(length*i)
        # print start+(length*i)+(length-i)-1
        # print xor(start+(length*i), start+(length*i)+(length-i)-1)
        res ^= xor(start+(length*i), start+(length*i)+(length-i)-1)
        # print '-'
    return res