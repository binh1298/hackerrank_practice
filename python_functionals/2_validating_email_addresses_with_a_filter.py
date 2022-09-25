import re


def fun(s):
    return re.match(r'\b[A-Za-z0-9._-]+@[A-Za-z0-9]+\.[A-Z|a-z]{1,3}\b', s)


def filter_mail(emails):
    return list(filter(fun, emails))


standard_input = """3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com"""

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
