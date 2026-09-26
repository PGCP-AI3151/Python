days = int(input("Enter Number of Days: "))
start_day = int(input("0.Monday\n1.Tuesday\n2.Wednesday\n3.Thursday\n4.Friday\n5.Saturday\n6.Sunday\nEnter Start Day :-"))

if start_day < 0 or start_day > 6:
    print("Start Day must be between 0 and 6")
    exit()

print("-----Calendar-----")
print("Mon\tTue\tWed\tThu\tFri\tSat\tSun")

print("\t"*start_day,end=" ")

for j in range(days):
    if (start_day+j) % 7 == 0:
        print("")
    print(j+1, "\t", end="")
