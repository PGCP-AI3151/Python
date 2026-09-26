num = int(input("Enter a number: "))
evenDigits = 0
oddDigits = 0
sumDigits = 0
while num > 0:
    reminder = num % 10
    if reminder % 2 == 0:
        evenDigits += 1
    else:
        oddDigits += 1
    sumDigits+=reminder
    num = num // 10

print("Total Digits :-",evenDigits + oddDigits)
print("Even Digits-:-",evenDigits)
print("Odd Digits-:-",oddDigits)
print("Sum :-",sumDigits)