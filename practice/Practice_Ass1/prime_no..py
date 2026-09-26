start = int(input("Enter start no. :"))
end = int(input("Enter end no. :"))

print(f"prime no. between {start} and {end}")

for i in range(start, end+1):
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)


