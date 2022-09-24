import functools


def comparator(firstMap, secondMap):
    if (firstMap[k] >= secondMap[k]):
        return 1
    else:
        return -1


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    [print(*numList)
     for numList in sorted(arr, key=functools.cmp_to_key(comparator))]
