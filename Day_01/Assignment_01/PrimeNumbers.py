
start = int(input("Enter Start :- "))
end = int(input("Enter End :- "))


print(f"-----Prime Numbers (Between {start} and {end})-----")
for i in range(start, end+1):
    j = 2
    while j < i:
        if i % j == 0:
            break
        j+=1

    else:
        print(i)