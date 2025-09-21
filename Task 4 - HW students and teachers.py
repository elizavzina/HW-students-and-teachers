class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and  course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')
some_student = Student('Ruoy', 'Eman', 'male')
some_student_2 = Student('John', 'Brown', 'male')
students = []
students.extend(some_student, some_student_2)
def average_grade_by_students(students, course):
    all_grades_list = []
    for student in students:
        if course in student.courses_in_progress:
            all_grades_list.append(student.grades)
            return (f'Средняя оценка за курс {course} у всех студентов составляет{float(sum(all_grades_list) / len(all_grades_list))}')
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}')
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer_2 = Lecturer('Any', 'Buddy')
lecturers = []
lecturers.extend(some_lecturer, some_lecturer_2)
def average_grade_by_lecturers(lecturers, course):
    all_grades_list = []
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            all_grades_list.append(lecturer.grades)
            return (f'Средняя оценка за курс {course} у всех лекторов составляет{float(sum(all_grades_list) / len(all_grades_list))}')
class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
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


some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer_2 = Reviewer('Someone', 'Else')

some_student.courses_in_progress += ['Python', 'Git']
some_student_2.courses_in_progress += ['Python', 'GitVerse']
some_student.finished_courses += ['Введение в программирование']
some_student_2.finished_courses += ['Введение в программирование', 'Git']
some_reviewer.courses_attached += ['Python', 'Git']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9.8)
some_reviewer.rate_hw(some_student_2, 'Python', 9)
some_reviewer.rate_hw(some_student_2, 'GitVerse', 8)
some_reviewer_2.courses_attached += ['Python', 'Git']
some_reviewer_2.rate_hw(some_student, 'Python', 10)
some_reviewer_2.rate_hw(some_student, 'Git', 9.8)
some_reviewer_2.rate_hw(some_student_2, 'Python', 9)
some_reviewer_2.rate_hw(some_student_2, 'GitVerse', 8)
some_lecturer.courses_attached += ['Python', 'Git']
some_lecturer_2.courses_attached += ['Git', 'GitVerse']
some_student.rate_lecture(some_lecturer, 'Python', 9.9)
some_student.rate_lecture(some_lecturer, 'Git', 9.9)
some_student.rate_lecture(some_lecturer_2, 'Python', 9)
some_student.rate_lecture(some_lecturer_2, 'Git', 10)
some_student_2.rate_lecture(some_lecturer, 'Python', 9.3)
some_student_2.rate_lecture(some_lecturer, 'Git', 9.7)
some_student_2.rate_lecture(some_lecturer_2, 'Python', 9)
some_student_2.rate_lecture(some_lecturer_2, 'GitVerse', 10)

print(some_reviewer)
print(some_reviewer_2)
print(some_lecturer)
print(some_lecturer_2)
print(some_student)
print(some_student_2)
average_grade_by_students(students, 'Python')
average_grade_by_students(students, 'Git')
average_grade_by_students(students, 'GitVerse')
average_grade_by_lecturers(lecturers, 'Python')
average_grade_by_lecturers(lecturers, 'Git')
average_grade_by_lecturers(lecturers, 'GitVerse')
