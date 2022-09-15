import itertools


standard_input = """3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 """

n, m = map(int, input().split())

original = [list(map(int, input().split()))[1:] for i in range(n)]
squared = [[num * num for num in s] for s in original]

print(max([sum(group) % m
           for group in list(itertools.product(*squared))]))
