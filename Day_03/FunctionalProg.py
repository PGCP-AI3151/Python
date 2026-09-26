from functools import reduce

from Viraj_Vikram.Day_02.ListComprehension import square

data = ['pat','that','matter','hello','hat','sites']
data.sort()
print(data)

data.sort(reverse=True)
print(data)

data.sort(key = lambda x : len(x))
print(data)

min_s = min(data)
print(min_s)

min_s = min(data,key = lambda x : len(x))
print(min_s)

max_s = max(data)
print(max_s)

max_s = max(data,key = lambda x : len(x))
print(max_s)

numbers = [1,3,4,5,6,2,3,7,8]

squares = list(map(lambda x : x*x,numbers))
print(squares)

even = list(filter(lambda x : x%2 ==0 ,numbers))
print(even)

total = reduce(lambda x,y : x+y,numbers)
print(total)

s_upper = list(map(lambda x : x.upper(),data))
print(s_upper)

start_with_h = list(filter(lambda x : x.startswith('h'),data))
print(start_with_h)