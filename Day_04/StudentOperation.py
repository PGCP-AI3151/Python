class Operation:

    @staticmethod
    def print_students(Students):
        for i in Students:
            print(i)

    @staticmethod
    def search_student(Students, Id):
        for i in Students:
            if i.roll == Id:
                print(i)
                break
        else:
            print(f'Roll No :- {Id} || Student not found !!')

    @staticmethod
    def calculate_gpa(Students):
        for i in Students:
            m1, m2, m3 = map(int,i.marks)
            gpa = (1/3) * m1 + (1/2) * m2 + (1/4) * m3
            print(i , f'| GPA : {gpa/10 :.2f}')

    @staticmethod
    def sort_student(Students):
        sorted_student = sorted(Students, key=lambda student : student.name)
        for i in sorted_student:
            print(i)