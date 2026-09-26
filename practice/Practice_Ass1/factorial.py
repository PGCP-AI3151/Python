num = int(input("Enter no. between 0! to 10! :"))

factorial = 1
for n in range(0, num+1):
    if n == 0:
        factorial = 1
    else:
        factorial *= n

print(f"{n}! : {factorial}")