def wrapper(sort_phone):
    def standardize(phoneNum: str):
        if (phoneNum.startswith("0")):
            return f"+91 {phoneNum[1:6]} {phoneNum[6::]}"
        if (phoneNum.startswith("+91")):
            return f"+91 {phoneNum[3:8]} {phoneNum[8::]}"
        elif (len(phoneNum) == 10):
            return f"+91 {phoneNum[0:5]} {phoneNum[5::]}"
        elif (len(phoneNum) == 12):
            return f"+91 {phoneNum[2:7]} {phoneNum[7::]}"
        return phoneNum

    def fun(phoneNums: "list[str]"):
        sort_phone([standardize(phoneNum) for phoneNum in phoneNums])

    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


standard_input = """4
07895462130
919875641230
9195969878
+911234512345"""
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
