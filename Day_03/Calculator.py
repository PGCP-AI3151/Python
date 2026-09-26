import Math
from Math import add,subtract,multiply,divide
from Math import multiply as mult

while True:

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print("-----Calculator-----\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n--------------------")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            res = Math.add(num1, num2)
            print('Addition :- ', res)

        case 2:
            res = Math.subtract(num1, num2)
            print('Subtraction :- ', res)

        case 3:
            res = Math.multiply(num1, num2)
            print('Multiplication :- ', res)

        case 4:
            res = Math.divide(num1, num2)
            print('Division :- ', res)

        case 5:
            print('Exiting..!!')
            exit()

        case _:
            print('Invalid Choice !!')

