def solution(X, Y):
    widest = 0
    x_sort = sorted(X)
    for i in range(len(x_sort)):
        if i == len(x_sort)-1:
            return widest
        ttl = x_sort[i+1] - x_sort[i]
        if ttl > widest:
            widest = ttl
    return wides
