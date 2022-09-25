def cube(x): return x**3


def fibonacci(n):
    result = [False for _ in range(n + 1)]

    def fib(t):
        if (result[t] is not False):
            return result[t]
        elif (t == 0):
            result[t] = 0
        elif (t == 1):
            result[t] = 1
        else:
            result[t] = fib(t-1) + fib(t-2)

        return result[t]

    fib(n)

    return result[:-1]


standard_input = """5"""
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
