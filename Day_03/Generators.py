def get_number():
    i = 0
    while True:
        yield i
        i+=1

series = get_number()
print(next(series))
print(next(series))
print(next(series))
print(next(series))
print(next(series))

def get_fib(end):
    i = 0
    a,b = 0,1
    while i < end:
        yield b
        a,b = b, a+b
        i+=1

fib_series = get_fib(20)
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))
print(next(fib_series))

for i in range(14):
    print(next(fib_series))

