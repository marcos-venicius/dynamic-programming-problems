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

def canSum(target, nums, memo = {}):
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for n in nums:
        if canSum(target - n, nums, memo):
            memo[target] = True
            return True

    memo[target] = False

    return False


tests = [
    (7,     [2, 3],         True),
    (7,     [5, 3, 4, 7],   True),
    (6,     [5],            False),
    (7,     [2, 4],         False),
    (8,     [2, 3, 5],      True),
    (7,     [1],            True),
    (300,   [14, 7],        False),
    (900,   [14, 7],        False),
]

def test1():
    for test in tests:
        # for some reason if i remove the '{}' from the params
        # the method is keeping the value between the calls
        # i'm not sure why lol
        r = canSum(test[0], test[1], {})

        assert r == test[2], f"({test[0]}, {test[1]}) should be {test[2]} (!= {r})"

duration(test1)
