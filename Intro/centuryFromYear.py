#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(year: int) -> int:
    if ((year % 100) - 1) >= 0:
        return int(year / 100) + 1
    return int(year / 100)


if __name__ == '__main__':
    years = [1905, 1700, 1988, 2000, 2001, 200, 374, 45, 8]
    for year in years:
        print(solution(year))
