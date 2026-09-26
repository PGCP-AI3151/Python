t1 = (1,2,3,4)
t2 = (3,5,2,1)
t3 = (2,2,3,1)

res =[]
zipped = tuple(zip(t1,t2,t3))
for i in zipped:
    sum = 0
    for j in i:
        sum += j
    res.append(sum)
print(tuple(res))
