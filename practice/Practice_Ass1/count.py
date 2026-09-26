num = int(input("Enter no.:"))

Count_Digit = 0
Even_Digit = 0
odd_Digit = 0
digit_sum = 0

while num > 0:
    Count_Digit = Count_Digit + 1
    digit = num % 10

    digit_sum += digit

    if digit % 2 == 0:
        Even_Digit +=1

    num = num // 10

odd_Digit = Count_Digit - Even_Digit


print(f"No. of Digit: {Count_Digit}")
print(f"Even Digit: {Even_Digit}")
print(f"odd digit: {odd_Digit}")
print(f"sum: {sum}")
