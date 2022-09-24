def isPalindrome(inputString: str) -> bool:
    firstCharIndex = 0
    lastCharIndex = len(inputString) - 1

    while (firstCharIndex < lastCharIndex):
        if (inputString[firstCharIndex] != inputString[lastCharIndex]):
            return False
        else:
            firstCharIndex += 1
            lastCharIndex -= 1
    return True


standard_input = """5
12 61 65656 14"""
n = input()
arr = input().split()

firstCondition = all([i > 0 for i in map(int, arr)])
secondCondition = any([isPalindrome(i) for i in arr])

print(firstCondition and secondCondition)
