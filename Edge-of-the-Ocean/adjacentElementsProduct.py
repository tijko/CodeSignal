#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(inputArray: [int]) -> int:
    high_prod = inputArray[0] * inputArray[1]
    for i,v in enumerate(inputArray[:-1]):
        current_prod = inputArray[i+1] * v
        if current_prod > high_prod:
            high_prod = current_prod
    return high_prod


if __name__ == '__main__':
    arrays = [
              [3, 6, -2, -5, 7, 3],
              [-1, -2],
              [5, 1, 2, 3, 1, 4],
              [1, 2, 3, 0],
              [9, 5, 10, 2, 24, -1, -48],
              [5, 6, -4, 2, 3, 2, -23],
              [4, 1, 2, 3, 1, 5],
              [-23, 4, -3, 8, -12],
              [1, 0, 1, 0, 1000]
             ]
    for array in arrays:
        print(solution(array)) 
