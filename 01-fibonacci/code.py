#!/usr/bin/env python3

from time import time

# 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13
def fib(n):
    n1 = 1
    n2 = 1

    for _ in range(n - 1):
        tmpN1 = n1
        n1 = n2
        n2 = tmpN1 + n2

    return n1

def fibRecursive(n):
    if n <= 2:
        return 1

    return fibRecursive(n - 1) + fibRecursive(n - 2)


tests = [
    (10, 55),
    (20, 6765),
    (30, 832040),
    (40, 102334155)
    # more large number will take so much time
]

def test1():
    print("using for loop: ")
    start = time()

    for test in tests:
        assert fib(test[0]) == test[1], f"num: {test[0]} should be equal to {test[1]}"

    end = time()

    r = end - start
    print(f"{r:.5f}s")

def test2():
    print("using recursion: ")
    start = time()

    for test in tests:
        assert fibRecursive(test[0]) == test[1], f"num: {test[0]} should be equal to {test[1]}"

    end = time()

    r = end - start
    print(f"{r:.5f}s")

test1()
test2()
