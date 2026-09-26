data =['pat','bat','mat','sat','rat','fat']

print('fat' in data)
print('that' not in data)

for item in data:
    print(item.upper())

print(len(data))
print(data[0])
print(data[1:5])
print(data[-2])
print(data[1:5])
print(data[1:5:2])
print(data[-1:-5])
print(data[:2] + data[2:])

print(data.append('rat'))
print(data)

data.insert(3, 'viraj')
print(data)

pos = data.index('viraj')
print(pos)

data.append(['Vikram','Raj'])
print(data)

data.extend(['priyanshu','harshith'])
print(data)

data.remove(['Vikram','Raj'])
print(data)
# data.remove('pat')
# print(data)

print(data.count('pat'))
data.pop(4)
print(data)
# data.remove(['that','kat'])
data.sort()
print(data)
# sorted_array = sorted(data)
# print(sorted_array)
data.reverse()
print(data)

for index,value in enumerate(data):
    print(f"{index} -- {value}")

my_list = [[11,'One'],[2,'Two'],[3,'Three']]
for item in my_list:
    print(item)

for num,value in enumerate(my_list):
    print(f"{num} -- {value}")

for num,value in (my_list):
    print(f"{num} -- {value}")

my_list.sort()
print(my_list)

my_list.sort(reverse = True)
print(my_list)

