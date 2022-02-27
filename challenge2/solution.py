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
        if reminder == 1:
            reminder = 2
        elif reminder == 2:
            reminder = 1
        if flag:
            x = 0
            for i in sorted(l):
                if i % 3 == reminder and x < 2:
                    l.remove(i)
                    x = x + 1
                    flag = False
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