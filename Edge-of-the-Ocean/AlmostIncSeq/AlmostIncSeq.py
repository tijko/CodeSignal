#!/usr/bin/env python
# -*- coding: utf-8 -*-


def increasing(seq: [int]) -> bool:
    for i,v in enumerate(seq[:-1]):
        if v >= seq[i+1]:
            return False
    return True

def solution(seq: [int]) -> bool:
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
