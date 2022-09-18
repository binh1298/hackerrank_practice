import re
standard_input = """2
.*\+
.*+"""

t = int(input())
for i in range(t):
    try:
        re.compile(input())
        print(True)
    except:
        print(False)
