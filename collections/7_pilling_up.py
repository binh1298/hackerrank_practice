from collections import deque

standard_input = """2
6 
4 3 2 1 3 4
3
1 3 2"""
t = int(input())


def solve(currentDeQueue: "deque[int]", currentBase: int, path: str):
    if (len(currentDeQueue) == 0):
        # print(path)
        return True

    leftMost = currentDeQueue[0]
    rightMost = currentDeQueue[len(currentDeQueue) - 1]

    if (currentBase < leftMost and currentBase < rightMost):
        return False

    flagLeft = False
    if (currentBase >= leftMost):
        clonedQueueLeft = deque(list(currentDeQueue))
        clonedQueueLeftBase = clonedQueueLeft.popleft()
        flagLeft = solve(clonedQueueLeft, clonedQueueLeftBase, f"{path}Left")

    if (flagLeft):
        return True

    flagRight = False
    if (currentBase >= rightMost):
        clonedQueueRight = deque(list(currentDeQueue))
        clonedQueueRightBase = clonedQueueRight.pop()
        flagRight = solve(clonedQueueRight,
                          clonedQueueRightBase, f"{path}Right")
    if (flagRight):
        return True


def solve2(currentDeQueue: "deque[int]", beginningBase: int, test: str):
    currentBase = beginningBase
    while len(currentDeQueue) > 0:
        leftMost = currentDeQueue[0]
        rightMost = currentDeQueue[len(currentDeQueue) - 1]

        if (currentBase < leftMost and currentBase < rightMost):
            return False

        if (leftMost >= rightMost and leftMost <= currentBase):
            currentBase = leftMost
            currentDeQueue.popleft()
            continue

        if (leftMost <= rightMost and rightMost <= currentBase):
            currentBase = rightMost
            currentDeQueue.pop()
            continue

        return False

    return True


for i in range(t):
    n = int(input())
    queue = deque(map(int, input().split()))
    if (solve2(queue, max([queue[0], queue[len(queue) - 1]]), "")):
        print("Yes")
    else:
        print("No")
