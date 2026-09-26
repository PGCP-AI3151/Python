from CarPortal import Car

c1 = Car('Honda','city',2000000)
c2 = Car('Tata','safari',5000000)

print(c1)
print(c1.calculate_premium(3))
print(c2.calculate_premium(5))

Car.show_count()

c1._price = 2200000
print(c1)

c1.price = 500
print(c1)

data = 'kia,seltos,150000'
c3 = Car.from_string(data)
print(c3)
print(type(c3))

c4 = eval(repr(c2))
print(c4)
print(type(c4))