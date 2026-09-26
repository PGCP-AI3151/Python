# name = input("Enter your name :- ")
# age = int(input("enter your age :- "))
#
# print("You entered Name : ",name,"and Age :",age)
# print('You Entered Name : {} and Age : {}'.format(name,age))
# print(f"You Entered Name : {name} and Age :{age}")
#
data = 55
print(f"{data :05d}")

data = 4e+6
print(data)
print(f"{data : ,.2f}")

data = 4e-6
print(data)
print(f"{data : .6f}")

data =1000000
print(data)
print(f"{data : ,.2f}")

data = 0.65
print(f"{data : .0%}")
print(f"{data : .2%}")

name = "abc"
print(f"{name:<10}")
print(f"{name:>10}")
print(f"{name:^10}")

