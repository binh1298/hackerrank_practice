consonants = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = "AEIOU"

string = input()
sLength = len(string)
stuartPoints = 0
kevinPoints = 0


i = 0
for c in string:
    if (consonants.find(c) != -1):
        stuartPoints += sLength - i
    if (vowels.find(c) != -1):
        kevinPoints += sLength - i
    i += 1

if (stuartPoints == kevinPoints):
    print("Draw")
elif (stuartPoints > kevinPoints):
    print(f"Stuart {stuartPoints}")
else:
    print(f"Kevin {kevinPoints}")
