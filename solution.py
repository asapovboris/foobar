def solution(l):
    sum_digits = sum(l)
    if sum_digits < 3:
        return '0'
    reminder = sum_digits % 3
    flag = True
    while flag and reminder:
        for i in sorted(l):
            if i % 3 == reminder:
                l.remove(i)
                flag = False
                break
        if reminder == 2 and flag:
            for i in sorted(l):
                if i % 3 == reminder - 1:
                    l.remove(i)
                    l.remove(i)
                    flag = False
                    break
        elif flag:
            flag = False
            l = 0
    if l:
        l = sorted(l, reverse=True)
        string_ints = [str(int) for int in l]
        str_of_ints = "".join(string_ints)
        return str_of_ints
    else:
        return '0'
