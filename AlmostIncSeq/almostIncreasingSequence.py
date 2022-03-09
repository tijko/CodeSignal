    test = sequence[:]
    count = 0
    for i,v in enumerate(sequence):
        test.pop(i)
        for j,c in enumerate(test[:-1]):
            if test[j+1] <= c:
                count += 1
                break
        test = sequence[:]
    return count != len(sequence)
