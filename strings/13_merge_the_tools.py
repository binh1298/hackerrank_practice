string = input()
k = int(input())

sLength = len(string)
i = 0
sArr = []
for i in range(sLength//k):
    sArr.append(string[(k*i):(k*i+k)])
    i += 1


def uniq(string):
    result = ""
    resultMap = {}
    for c in string:
        if (c in resultMap):
            continue

        resultMap[c] = True
        result = result + c

    return result


for u in sArr:
    print(uniq(u))
