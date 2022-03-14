#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(matrix: [[int]]) -> int:
    # number of floors
    length = len(matrix)
    total = 0
    matching = list(range(len(matrix[0])))
    ghosts = list()
    for i in range(length):
        for j in matching:
            if j in ghosts: continue
            if matrix[i][j] == 0:
                ghosts.append(j)
            else:
                total += matrix[i][j]
    return total


if __name__ == '__main__':
    matrices = [
                [[0,1,1,2], 
                 [0,5,0,0], 
                 [2,0,3,3]],
                [[1,1,1,0], 
                 [0,5,0,1], 
                 [2,1,3,10]],
                [[1,1,1], 
                 [2,2,2], 
                 [3,3,3]],
                [[0]],
                [[1,0,3], 
                 [0,2,1], 
                 [1,2,0]],
                [[1], 
                 [5], 
                 [0], 
                 [2]],
                [[1,2,3,4,5]],
                [[2], 
                 [5], 
                 [10]],
                [[4,0,1], 
                 [10,7,0], 
                 [0,0,0], 
                 [9,1,2]],
                [[1]]
               ]
    for matrix in matrices:
        print(solution(matrix))
