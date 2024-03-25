class GeeksPeople:
    def __init__(self, name, email, phone ) :
        self.name = name 
        self.email = email
        self.phone = phone
    
    def __str__(self) -> str:
        return f'Имя - {self.name}, почта - {self.email}, номер телефона: {self.phone}'
    
class Student(GeeksPeople):
    def __init__(self, name, email, phone, student_id, group_where_study, ):
        GeeksPeople.__init__(self, name, email, phone)
        self.student_id = student_id
        self.group_where_study = group_where_study

    def study(self):
        print(f'Cтудент {self.name} учиться в группе {self.group_where_study}')

    def __str__(self) -> str:
        return f'Имя студента - {self.name}, почта - {self.email}, номер телефона: {self.phone}, Id - {self.student_id}, Группа студента - {self.group_where_study}'


class Teacher(GeeksPeople):
    def __init__(self, name, email, phone, teacher_id, group_where_teach ):
        GeeksPeople.__init__(self,name, email, phone)
        self.teacher_id = teacher_id
        self.group_where_teach = group_where_teach

    def teach(self):
        print(f'Учитель {self.name} преподаёт в группе {self.group_where_teach}')

    def __str__(self) -> str:
        return f'Имя учителя - {self.name}, почта - {self.email}, номер телефона: {self.phone}, Id - {self.teacher_id}, преподаёт в группе - {self.group_where_teach}'



class Admin(GeeksPeople):
    def __init__(self, name, email, phone, admin_id, new_group):
        GeeksPeople.__init__(self, name, email, phone)
        self.admin_id = admin_id
        self.new_group = new_group
    def create_group(self):
        print(f'Администратор {self.name} создал новую группу {self.new_group}')

    def __str__(self) -> str:
        return f'Имя администратора - {self.name}, почта - {self.email}, номер телефона: {self.phone}, Id - {self.admin_id}'
    

class Mentor(Student, Teacher):
    pass

student = Student("Ainazik", "ainazikerkinbaeva@gmail.com", "0550633963", "№1", "16-1")
print(student)
student.study()

teacher = Teacher("Syimyk", "syimykabdykadurov@gmail.com", "0777567645", "№1", "16-1")
print(teacher)
teacher.teach()

admin = Admin("Nurbolot", "erkinbaevnurbolot@gmail.com", "+996 558 000 350", "№1", "15-2")
print(admin)
admin.create_group()

mentor = Mentor("Nurai", "nuraikaa@gmail.com", "0776545578", "№1", "12-1" )
print(mentor)
mentor.study()


