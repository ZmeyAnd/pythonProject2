students_list = []
lectors_list = []
def average(num):
    res = []
    for value in num.values():
        res += value
    return sum(res) / len(res)



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)


    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average(self.grades)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'
    def __lt__(self, other):
        return average(self.grades) < average(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lectors_list.append(self)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average(self.grades)}'

    def __lt__(self, other):
        return average(self.grades) < average(other.grades)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'



best_student = Student('Ruoy', 'Eman', 'your_gender')
bad_student = Student('Ivan', 'Durak', 'm')
bad_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Python', 'Git']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git', 'Java']
cool_reviewer.rate_hw(bad_student, 'Python', 2)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 9)

cool_lector = Lecturer('Super', 'Man')
cool_lector.courses_attached += ['Python']
bad_student.rate_hw(cool_lector, 'Python', 4)
c_lector = Lecturer('Roma', 'Juk')
c_lector.courses_attached += ['Python', 'Git']
best_student.rate_hw(c_lector, 'Python', 10)
best_student.rate_hw(c_lector, 'Git', 10)

def rate_course(persons, course):
    res = []
    if persons == Student:
        for i in range(len(students_list)):
            if course in students_list[i].grades:
                res += students_list[i].grades[course]
        print(f'Средняя оценка за курс {course} составляет {round(sum(res) / len(res), 1)}')
    if persons == Lecturer:
        for i in range(len(lectors_list)):
            if course in lectors_list[i].grades:
                res += lectors_list[i].grades[course]
        print(f'Средняя оценка за курс {course} составляет {round(sum(res) / len(res), 1)}')



print(cool_reviewer)
print()
print(cool_lector)
print()
print(c_lector)
print()
print(best_student)
print()
print(bad_student)
print()
rate_course(Student, 'Git')
rate_course(Lecturer, 'Python')
print()
print('best_student > bad_student ==>', best_student > bad_student)
print('c_lector < cool_lector ==>', c_lector < cool_lector)

