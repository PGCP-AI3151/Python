
emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
        'Aditi': ['Python', 'PHP', 'Database']}

def printEmployee(employee):
    for name,skill in employee.items():
        print(f'{name} :- {','.join(skill)}')

print('-----Employee Know Python-----')
pythonDev = [emp  for emp,skill in emp_data.items() if 'Python' in skill ]
print(*pythonDev)

print('-----Add New Skill in All \'test\' Employee-----')
for emp in emp_data.keys():
    emp_data[emp].append('test')
printEmployee(emp_data)

print('-----Sort Employees By Skill-----')
sorted_emp = dict(sorted(emp_data.items(), key=lambda item : len(item[1]),reverse=True))
printEmployee(sorted_emp)