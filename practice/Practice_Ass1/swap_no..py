num = int(input("Enter 3 digit no.:"))

print(f"original no. {num}")

ones = num % 10
tens = (num // 10) % 10
hundreds = num // 100

swapped = (ones*100) + (tens*10) + hundreds

print(f"swapped no. is {swapped}")