#!/usr/bin/env python3

from time import time

def traveler(rows, cols, memo = {}):
    if rows == 0 or cols == 0:
        return 0

    if cols == 1 and rows == 1:
        return 1

    key = f'{rows}x{cols}'

    if key  in memo:
        return memo[key]

    down = traveler(rows - 1, cols, memo)
    right = traveler(rows, cols - 1, memo)

    memo[f'{rows - 1}x{cols}'] = down
    memo[f'{rows}x{cols - 1}'] = right

    return down + right

def traveler2(rows, cols, memo = {}):
    if rows == 0 or cols == 0:
        return 0

    if cols == 1 and rows == 1:
        return 1

    key = rows * cols

    if key  in memo:
        return memo[key]

    down = traveler(rows - 1, cols, memo)
    right = traveler(rows, cols - 1, memo)

    downKey = (rows - 1) * cols
    rightKey = rows * (cols - 1)
    
    memo[key] = down + right
    memo[downKey] = down
    memo[rightKey] = right

    return memo[key]

tests = [
    ((1, 1), 1),
    ((2, 3), 3),
    ((3, 3), 6),
    ((18, 18), 2333606220) # it takes a long time
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
