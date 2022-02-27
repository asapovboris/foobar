def solution(area):
    s = []
    x = 0
    while area > 0:
        if area < 4:
            s.append('1')
            area = area - 1
        elif area**.5 % 1 == 0:
            s.append(str(area))
            area = area - area + x
            x = 0
        else:
            area = area - 1
            x = x + 1
    return ','.join(s)