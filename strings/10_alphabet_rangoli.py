def print_rangoli(size):
    if (size == 1):
        print("a")
        return
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def generateLine(start):
        lineRight = "-".join([alphabet[i+1]for i in range(start, size - 1, 1)])
        lineLeft = "-".join([alphabet[i]for i in range(size - 1, start, -1)])
        line = "-".join([lineLeft, alphabet[start], lineRight])
        return line

    middleLine = generateLine(0)
    width = len(middleLine)

    for i in range(size - 1, 0, -1):
        line = generateLine(i).center(width, "-")
        print(line)

    print(middleLine)

    for i in range(1, size):
        line = generateLine(i).center(width, "-")
        print(line)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
