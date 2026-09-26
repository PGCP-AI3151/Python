l1 = lambda n : n+1
print(l1(1))

l2 = lambda n : n>100
print(l2(99))

l3  = lambda n1,n2 : n1+n2
print(10,5)

l6 = lambda n1,n2 ,n3=1 : n1+n2+n3
print(l6(10,20,30))
print(l6(10,20))


l4 = lambda *args : sum(args)
print(l4(10,20,30))

l5 = lambda **kwargs : sum(kwargs.values())
print(l5(one =1,two =2,three =3))