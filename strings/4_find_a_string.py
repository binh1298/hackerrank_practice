def count_substring(string, sub_string):
    subStringIndex = string.find(sub_string)
    if (subStringIndex != -1):
        return count_substring(string[subStringIndex + 1:], sub_string) + 1
    else:
        return 0


if __name__ == '__main__':
    print(len("1"))
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
