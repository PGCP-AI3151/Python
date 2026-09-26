for i in range(10):
    print(i,end=" ")

print("\n----------")
for i in range(1,11,2):
    print(i,end=" ")

print("\n----------")
for i in range(10):
    if i==5:
        continue
    print(i,end=" ")

print("\n----------")
num = int(input("Enter a Number :- "))
flag = True
for i in range(2,num):
    if num % i == 0:
        flag = False
        break
if flag:
    print("Prime")
else:
    print("Not Prime")

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")


