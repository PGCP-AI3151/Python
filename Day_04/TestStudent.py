from StudentDetails import Student
from StudentOperation import Operation

s1 = Student(1,'Viraj',[98,82,85])
s2 = Student(2,'Vikram',[82,79,75])
s3 = Student(3,'Harsh',[97,82,90])
s4 = Student(4,'Abhi',[77,61,86])
s5 = Student(5,'Krish',[90,86,75])

Students = [s1,s2,s3,s4,s5]
obj = Operation()

print('-----Student Details-----')
obj.print_students(Students)

print('-----Search Student-----')
obj.search_student(Students,0)

print('-----Calculate GPA Of Students-----')
obj.calculate_gpa(Students)

print('-----Sort Student By Name----')
obj.sort_student(Students)

