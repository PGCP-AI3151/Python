s1 = input("Enter a string: ")

flag = False
for ch in s1:
    if 'A' <= ch <= 'Z':
        flag = True
        break

if flag:
        print("All Letters Of String is in Uppercase !!")

else:
        print("All Letters Of String is not in Uppercase !!")