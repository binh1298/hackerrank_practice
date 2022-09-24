

standard_input = """Sorting1234"""

inputString: str = input()

lowerCaseString = ""
upperCaseString = ""
oddDigits = ""
evenDigits = ""

for char in inputString:
    if (char.isalpha()):
        if (char.isupper()):
            upperCaseString = upperCaseString + char
        elif (char.islower()):
            lowerCaseString = lowerCaseString + char
    elif (char.isnumeric()):
        if (int(char) % 2 == 0):
            evenDigits = evenDigits + char
        else:
            oddDigits = oddDigits + char

result = [*sorted(lowerCaseString), *sorted(upperCaseString),
          *sorted(oddDigits), *sorted(evenDigits)]
print("".join(result))
