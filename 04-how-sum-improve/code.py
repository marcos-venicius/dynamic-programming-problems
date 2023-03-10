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

# store the result of current target sum to memo
# if already has the result to the current targetSum, just return it
# if not, compute.
def howSum(targetSum = 0, array = [], memo = {}):
    if targetSum in memo: return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for n in array:
        remainder = targetSum - n
        result = howSum(remainder, array, memo)

        if result is not None:
            memo[targetSum] = result + [n]
            return memo[targetSum]
        else:
            memo[targetSum] = None

    memo[targetSum] = None

    return None

tests = [
    ((0,    []),                []),
    ((7,    [ 5, 3, 4, 7 ]),    [4, 3]),
    ((8,    [ 2, 3, 5 ]),       [2, 2, 2, 2]),
    ((7,    [ 2, 4 ]),          None),
    ((7,    [ 2, 3 ]),          [3, 2, 2]),
    ((100,  [ 1 ]),             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),
    ((300,  [ 7, 14 ]),         None),
]

def test1():
    for test in tests:
        ts = test[0][0]
        a = test[0][1]
        e = test[1]

        r = howSum(ts, a, {})

        assert str(e) == str(r), f"{r} is not equal to {e}"

    print("[+] all tests passed")

duration(test1)

