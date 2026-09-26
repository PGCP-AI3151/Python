s = "Python is Simpler Language"

print("Python" in s)
print("Java" not in s)

for ch in s:
    print(ch,end=" ")

print("\n")
for i in range(len(s)):
    print(s[i],end="")

print("\n-----String Slicing-----")
print(s[::-1])
print(s[-21:-27:-1])
print(s[18:])
print(s[0])
print(s[-1])


