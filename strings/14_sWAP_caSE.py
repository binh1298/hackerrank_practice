s = input()

result = ""
for c in s:
    if (c.isupper()):
        result = result + c.lower()
    else:
        result = result + c.upper()

print(result)
