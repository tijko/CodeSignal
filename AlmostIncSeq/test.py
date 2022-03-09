#!/usr/bin/env python
# -*- coding: utf-8 -*-


def increasing(seq):
    for i,v in enumerate(seq[:-1]):
        if v >= seq[i+1]:
            return False
    return True

def solution(seq):
    for i,v in enumerate(seq[:-1]):
        if v >= seq[i+1]:
            test = seq[:]
            test.pop(i)
            # test on removal here or next
            if increasing(test):
                return True
            test = seq[:]
            test.pop(i+1)
            if increasing(test):
                return True
            return False
    return True


if __name__ == '__main__':
    #t = [3,5,67,98,3]
    #t = [1,2,1,2]
    #t = [123,-17,-5,1,2,3,12,43,45]
    t = [1,2,3,4,99,5,6]
    if solution(t):
        print('True')
    else:
        print('False')
