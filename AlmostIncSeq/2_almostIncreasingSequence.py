def increasing_series(series):
    for i,v in enumerate(series[:-1]):
        for j in series[i+1:]:
            if v >= j:
                return False
    return True

def solution(sequence):
    test = sequence[:]
    for i in range(len(sequence)):
        test.pop(i)
        if increasing_series(test):
            return True
        test = sequence[:]
    return False
