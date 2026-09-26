from Viraj_Vikram.Day_02.List import my_list
num = [1,2,3,4,5,6]

for n in num:
    square = n**2
    print(square)

even = [n for n in num if n%2 == 0 ]
print(even)

even_odd= ["even" if n % 2 == 0 else "odd" for n in num]
print(even_odd)

squares = [n*n for n in num]
print(squares)

even_sqr = [n*n for n in num if n % 2 == 0]
print(even_sqr)

data = ['pat','that','matter','hello']
word_len = [len(word) for word in data]
print(word_len)

my_list = [[11,'One'],[2,'Two'],[3,'Three'],[4,'Four']]
word_len = [len(word[1]) for word in my_list]
print(word_len)

def calculate_discount(price):
    return price * 0.85

price = [890,1000,1200,450,560,870]
discount = [calculate_discount(n) for n in price]
print(discount)

sentences = 'Was it the rat, I saw ?'
vowels = [ch for ch in sentences if ch in ['a','e','i','o','u']]
print(vowels)