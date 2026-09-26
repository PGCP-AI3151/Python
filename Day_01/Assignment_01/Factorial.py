num = int(input("Enter a number for 0! to 10! : "))

factorial = 1
for i in range(1,num+1 ):
    factorial *= i

print(f"Factorial {num}! :- {factorial}")