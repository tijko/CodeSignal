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

if __name__ == '__main__':
    tests = [
             [3,5,67,98,3],
             [1,2,1,2],
             [123,-17,-5,1,2,3,12,43,45],
             [1,2,3,4,99,5,6]
            ]
    for test in tests:
        if solution(test):
            print('True')
        else:
            print('False')
