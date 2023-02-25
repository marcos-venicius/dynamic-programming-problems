#!/usr/bin/env python3

def duration(fn):
    from time import time
    start = time()
    try:
        fn()
    finally:
        end = time()
        d = end - start
        print(f'duration: {d:.5f}s')

def canSum(target, nums):
    if target == 0:
        return True

    if target < 0:
        return False

    for n in nums:
        if n > target: # prevent negative results
            continue

        if canSum(target - n, nums):
            return True

    return False


tests = [
    (7,     [5, 3, 4, 7],   True),
    (6,     [5],            False),
    (7,     [2, 4],         False),
    (8,     [2, 3, 5],      True),
    (7,     [1],            True),
    (300,   [14, 7],        False) # this takes a long time
]

def test1():
    for test in tests:
        r = canSum(test[0], test[1])

        assert r == test[2], f"({test[0]}, {test[1]}) should be {test[2]} (!= {r})"

duration(test1)
