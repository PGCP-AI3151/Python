num = int(input("entter:"))
if num > 100:
    print("greater than 100")
else:
    print("less than 100")
print("end")

age = int(input("enter your age"))
gender = input("enter your gender")
if age > 18:
    if gender == "m":
        print("male")
    else:
        print("child")

if age > 18 and gender == "m":
    print("man")
elif age > 18 and gender =="f":
    print("women")
else:
    print("child")
