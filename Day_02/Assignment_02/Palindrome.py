s1 = input("Enter a string: ")
res=""
for ch in s1:
    if ch.isalnum():
        res +=ch.lower()

if res == res[::-1]:
    print("Palindrome !!")
else:
    print("Not Palindrome !!")