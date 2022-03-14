#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(statues: [int]) -> int:
    max_height = max(statues)
    min_height = min(statues)
    statue_set = set(statues)
    complete_set = set(range(min_height, max_height + 1))
    return len(complete_set.difference(statue_set))
    
    
if __name__ == '__main__':
    statues_list = [
                    [6, 2, 3, 8],
                    [0, 3],
                    [5, 4, 6],
                    [6, 3],
                    [1]
                   ]
    for statue in statues_list:
        print(solution(statue))
