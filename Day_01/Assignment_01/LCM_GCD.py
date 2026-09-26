num1 = int(input("Enter a number: "))
num2=int(input("Enter another number: "))


min_num = min(num1,num2)
max_num = max(num1,num2)

while min_num != 0:
    temp = min_num
    min_num = max_num % min_num
    max_num = temp

gcd = max_num
lcm = (num1*num2 // gcd)
print("GCD :- ",gcd)
print("LCM :- ",lcm)