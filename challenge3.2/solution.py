def solution(n):
    staircases = [1] + [0] * n
    print staircases
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            print j
            staircases[j] = staircases[j] + staircases[j - i]
            print staircases
    return staircases[n] - 1