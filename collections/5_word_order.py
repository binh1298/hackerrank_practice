from collections import OrderedDict
standard_input = """4
bcdef
abcdefg
bcde
bcdef"""

N = int(input())

ordered_dictionary = OrderedDict()
for i in range(N):
    word = input()
    if (word in ordered_dictionary):
        ordered_dictionary[word] = ordered_dictionary[word] + 1
    else:
        ordered_dictionary[word] = 1

print(len(ordered_dictionary))
[print(i, end=" ") for i in ordered_dictionary.values()]
