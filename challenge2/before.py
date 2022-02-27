L = [3, 1, 4, 1, 5, 9]

sum_digits = sum(L)
print sum_digits
reminder = sum_digits % 3
print reminder
flag = True
while flag and reminder:
    for i in sorted(L):
        if i % 3 == reminder:
            print i
            L.remove(i)
            flag = False
            break
    if reminder == 1:
        reminder = 2
    else:
        reminder = 1
    if flag:
        for i in sorted(L):
            if i % 3 == reminder-1:
                print i
                L.remove(i)
                L.remove(i)
                flag = False
                break
    elif flag:
        flag = False
        L = 0
if L:
    L = sorted(L, reverse=True)

    string_ints = [str(int) for int in L]
    str_of_ints = "".join(string_ints)
    print str_of_ints
else:
    print 0
