if __name__ == '__main__':
    s = input()
    hasAlphaNum = False
    hasAlpha = False
    hasDigits = False
    hasLowerCase = False
    hasUpperCase = False
    for c in s:
        hasAlphaNum = hasAlphaNum or c.isalnum()
        hasAlpha = hasAlpha or c.isalpha()
        hasDigits = hasDigits or c.isdigit()
        hasLowerCase = hasLowerCase or c.islower()
        hasUpperCase = hasUpperCase or c.isupper()

    print(hasAlphaNum)
    print(hasAlpha)
    print(hasDigits)
    print(hasLowerCase)
    print(hasUpperCase)
