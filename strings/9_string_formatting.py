def print_formatted(number):
    columnWidth = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(f"{i}".rjust(columnWidth), end=" ")
        print(f"{oct(i)[2:]}".rjust(columnWidth), end=" ")
        print(f"{hex(i)[2:]}".rjust(columnWidth).upper(), end=" ")
        print(f"{bin(i)[2:]}".rjust(columnWidth), end="\n")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
