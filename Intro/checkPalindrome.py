#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(inputString: str) -> bool:
    return inputString == inputString[::-1]
    

if __name__ == '__main__':
    strings = ['aabaa', 'abac', 'a', 'az', 'abacaba', 'z', 'aaabaaaa', 
               'zzzazzazz', 'hlbeeykoqqqqokyeeblh', 'hlbeeykoqqqokyeeblh']
    for string in strings:
        print(solution(string))
