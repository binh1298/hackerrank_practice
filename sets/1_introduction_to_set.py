def average(array):
    l = list(set(array))
    return format(sum(l) / int(len(l)), ".3f")


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
