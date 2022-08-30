if __name__ == '__main__':
    englishSubsTotal = int(input())
    englishSubs = list(map(int, input().split()))
    frenchSubTotal = int(input())
    frenchSubs = list(map(int, input().split()))

    englishSubsMap = {}
    for englishSub in englishSubs:
        englishSubsMap[englishSub] = True
    frenchSubsMap = {}
    for frenchSub in frenchSubs:
        frenchSubsMap[frenchSub] = True

    result = []
    [result.append(englishSub) for englishSub in englishSubs if (
        englishSub not in frenchSubsMap)]
    [result.append(frenchSub) for frenchSub in frenchSubs if (
        frenchSub not in englishSubsMap)]

    print(len(result))
