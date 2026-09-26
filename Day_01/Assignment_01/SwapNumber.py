num = int(input("Enter a number: "))
print("Number :- ",num)
reverse = 0
while num > 0:
    reverse = reverse * 10 + (num % 10)
    num = num // 10

print("Reversed :- ",reverse)