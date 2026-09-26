num = [1,2,3,4,5,6]

even_odd= {n:"even" if n % 2 == 0 else "odd" for n in num}
print(even_odd)

squares = {n:n*n for n in num}
print(squares)

data = ['pat','that','matter','hello']
word_len = {word:len(word) for word in data}
print(word_len)

def calculate_discount(price):
    return price * 0.85

books = [{'Python':890},
         {'Java':1200},
         {'DSA':1150}]

discounted = {item:calculate_discount(price) for book in books for item,price in book.items()}
print(discounted)

books = {'Python':890,
         'Java':1200,
         'DSA':1150}
print(books)
discounted = {item:calculate_discount(price) for item,price in books.items()}
print(discounted)