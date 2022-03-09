def increasing(seq):
    for i,v in enumerate(seq[:-1]):
        if v >= seq[i+1]:
            return False
    return True

def solution(sequence):
    # return on True
    test = sequence[:]
    for i,v in enumerate(sequence):
        test.pop(i)
        if increasing(test):
            return True
        test = sequence[:]
    return False
