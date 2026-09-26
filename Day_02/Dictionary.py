dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
}

print(dict)

# print(dict['one'])  // error  keyError
print(dict[1])

print(type(dict.keys()))
print(dict.values())
print(dict.items())
print("-----Keys-----")
for key in dict.keys():
    print(key)

print("-----Values-----")
for value in dict.values():
    print(value)

print("-----Items-----")
for key,value in dict.items():
    print(f"{key} --> {value}")

emp_data = {
    'name' : 'Vikram',
    'age' : 25,
    'salary' : 120000,
    'skills' : ['python','java']
}

capitals = {'India':'new delhi',
            'Japan':'tokyo',
            'France':'peris'
            }

print(emp_data['name'])

emp_data['age'] = 30
print(emp_data)

emp_data['phone no'] = '909867543'
print(emp_data)

emp_data.update({'salary':20000})
print(emp_data)

emp_data.pop('phone no')
print(emp_data)

print(emp_data.get('name'))

emp =sorted(dict.items(), key=lambda x: x[0])
print(emp)