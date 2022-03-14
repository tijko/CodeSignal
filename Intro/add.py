#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(param1: int, param2: int) -> int:
    return sum((param1,param2))

    
if __name__ == '__main__':
    tests = [(1,2), (0,1000), (2,-39), (99,100),
              (100,-100), (-1000,-1000)]
    for test in tests:
        print(solution(*test))
