#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(inputArray):
    total = 0
    idx = 0
    length = len(inputArray)
    while idx < (length - 1):
        a1, a2 = inputArray[idx], inputArray[idx+1]
        if inputArray[idx] >= inputArray[idx+1]:
            move = (a1 - a2) + 1
            total += move
            inputArray[idx+1] = a1 + 1
        idx += 1
    return total

if __name__ == '__main__':
    tests = [
             [1, 1, 1],
             [-1000, 0, -2, 0],
             [2, 1, 10, 1],
             [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]
            ]
    for test in tests:
        print(solution(test))
