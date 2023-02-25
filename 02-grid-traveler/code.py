#!/usr/bin/env python3

from time import time

def traveler(rows, cols, x = 0, y = 0):
    # return 0 when invalid grid
    if rows == 0 or cols == 0:
        return 0

    # if reached the end, return one more possibility
    if x == cols - 1 and y == rows - 1:
        return 1

    # if can't travel to the next column, travel to the next row
    if x == cols - 1:
        return traveler(rows, cols, x, y + 1)
    # if can't travel to the next row, travel to the next column
    if y == rows - 1:
        return traveler(rows, cols, x + 1, y)

    # if can travel to both, sum the travel to next column with the travel to the next row
    return traveler(rows, cols, x + 1, y) + traveler(rows, cols, x, y + 1)

def traveler2(rows, cols):
    if rows == 0 or cols == 0:
        return 0

    if cols == 1 and rows == 1:
        return 1

    return traveler(rows - 1, cols) + traveler(rows, cols - 1)

tests = [
    ((1, 1), 1),
    ((2, 3), 3),
    ((3, 3), 6),
    # ((18, 18), 2333606220) # it takes a long time
]

def duration(fn):
    start = time()
    try:
        fn()
    finally:
        end = time()
        d = end - start
        print(f'duration: {d:.5f}s')

def test1():
    print('using recursion')

    for test in tests:
        g = test[0]
        r = traveler(g[0], g[1])
        assert r == test[1], f"result should be {test[1]} (!= {r})"

def test2():
    print('using recursion')

    for test in tests:
        g = test[0]
        r = traveler2(g[0], g[1])
        assert r == test[1], f"result should be {test[1]} (!= {r})"

duration(test1)
duration(test2)
