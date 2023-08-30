def fib(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a


for i in fib(10):
    if i == 13:
        break
    print(i)
