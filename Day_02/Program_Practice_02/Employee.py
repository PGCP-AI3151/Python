emp_data = {'Amol': ['C', 'C++', 'Java'], 'Aditya': ['Angular', 'Java'],
            'Aditi': ['Python', 'PHP', 'Database']}

print('-----Employee Details-----')
for employee , skills in emp_data.items():
    print(f"{employee}: {', '.join(skills)}")

print('-----Employees Know Java-----')
java = [emp for emp,skills in emp_data.items() if 'Java' in skills]
print(*java)

print('-----Update Skill For an Amol-----')
skills = emp_data.get('Amol')
skills[0] = 'Python'
for employee , skills in emp_data.items():
    print(f"{employee}: {', '.join(skills)}")


print('-----Deleted Employee Amol-----')
emp_data.pop('Amol')
for employee , skills in emp_data.items():
    print(f"{employee}: {', '.join(skills)}")