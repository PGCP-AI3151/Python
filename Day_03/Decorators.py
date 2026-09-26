import time

from Viraj_Vikram.Day_02.Tuple import n2


def keep_time(inner):
    def wrapper():
        start = time.time()
        inner()
        end = time.time()
        print(f'Time taken: {end - start}')
    return wrapper

@keep_time
def print_square():
    for i in range(100):
        print(i*i)

print_square()

def smart_math(inner):
    def wrapper(*args, **kwargs):
        a,b = args
        if a < b:
            a,b = b,a
        return inner(a,b)
    return wrapper

@smart_math
def subtraction(n1 ,n2):
    return  n1-n2

print("Subtraction :- ",subtraction(2,10))