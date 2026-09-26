i = 5    # immutable
print(type(i))
print(i)
print(id(i))

j = 5
print(type(j))
print(j)
print(id(j))

print(i == j) # check values :- true :- if both object have same value
print(i is j) #check id :- true :- if both are the same object in memory

print(i)
print(id(i))
i = 5.5

print(i)
print(id(i))
print(type(i))

k = 'Hello'   # immutable
print(type(k))
print(k)
print(id(k))

v = 'Hello'
print(type(v))
print(v)
print(id(v))

t = (10,)  #immutable
print(type(t))
print(t)

s = {10, 20, 30} #immutable
print(type(s))
print(s)
print(id(s))

s2 = {10, 20, 30}
print(type(s2))
print(s2)
print(id(s2))

l = [10, 20, 30, 40]  # mutable
print(type(l))
print(l)
print(id(l))

l1 = [10, 20, 30, 40]

print(l == l1)  # True :- check values
print(l is l1)  # False :- check reference

d = {"One": 1, "Two": 2, "Three": 3} # mutable
print(type(d))
print(d)

x = 4
c = complex(i, x)
print(type(c))
print(c)
