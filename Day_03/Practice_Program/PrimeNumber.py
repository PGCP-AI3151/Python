
def generator():
    i = 2
    while True:
     for j in range(2, int(i**0.5)+1):
         if i % j == 0:
             break
     else:
         yield i
     i += 1

def create_prime_number(n):
    if n <= 0 :
        print("Please Enter a Positive Integer / None Zero Integer")
        return
    print(f'-----First {n} Prime Numbers-----')
    prime = generator()
    for i in range(n):
        print(next(prime))

if __name__ == "__main__":
    n = int(input("Enter a Positive Integer : "))
    create_prime_number(n)