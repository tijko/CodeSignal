#!/usr/bin/env python
# -*- coding: utf-8 -*-


#XXX Looking for constant time O(1) 
#    Holy Grail...
def solution(n: int) -> int:
  return (sum(range(n)) * 4) + 1 


if __name__ == '__main__':
    shapes = [2, 3, 1, 5, 7000, 8000, 9999, 9998, 8999, 100]
    for shape in shapes:
        print(solution(shape))
