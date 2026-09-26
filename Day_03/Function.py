def myFunction():
    print("Hello World")

myFunction()

def addition(a,b):
    return a+b

res = addition(3,4)
print('Result :-',res)

print(addition(3,4))
print(addition('a','b'))

def calculate_discount(product = 'Book',price = 200):
    price = price * 0.75
    print(f'Price of the {product} after discount : {price}')


calculate_discount('Pen',10)
calculate_discount(price=200,product='watch')
calculate_discount()
calculate_discount('Bag')
calculate_discount(price = 100)

"""
1. Positional Arguments : the dat type and sequence in which we pass the arguments must match the parameter list
2. keyword arguments : the dat type must be match but sequence in which we pass the arguments can change [given_as param_name = value]
3.Default Parameter : parameter in function can be assigned with default values. Once a param is given a default value all param
    that follow must be given a default value as well
"""

"""
1. Variable arguments : function receives a tuple
2. variable keyword arguments : function receives a dictionary
"""

def add(*num):
    res =0
    for n in num:
        res += n
    return res

print(f'Addition :- {add(10,20,30,40)}')
nums = [10,20,30,40,50]
print(f'Addition :- {add(*nums)}')

def calculate_average(**data):
    marks = data['marks']
    res = 0
    for mark in marks:
        res += mark
    return res/len(marks)
avg = calculate_average(name = 'Vikram', rollno = 20, marks = [10,20,30,40,50])
print(f'Average Marks :- {avg}')
student_data = {"name": "xyz",
                "marks":[90, 72, 80]}
avg = calculate_average(**student_data)
print(f"average marks : {avg: .2f}")