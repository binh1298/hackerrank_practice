if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxValue = -999
    secondMaxValue = -999
    for j in arr:
        if (maxValue < j):
            maxValue = j
    for i in arr:
        if (secondMaxValue < i and i != maxValue):
            secondMaxValue = i
    print(secondMaxValue)
