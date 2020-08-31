#!/usr/bin/env python3

def arrayManipulation(n, queries):
    current = 0
    localMax = 0
    mArray = [0] * (n + 1)
    for i in queries:
        mArray[i[0] - 1] += i[2]
        mArray[i[1]] -= i[2]

    for j in mArray:
        current += j
        if current > localMax:
            localMax = current
    return localMax


if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    print(result)

