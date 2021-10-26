student_list = []
lecturer_list = []
reviewer_list = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self)

    def average_grade(self):
        sum_hw = 0
        counter = 0
        for course in self.grades.values():
            for grade in course:
                sum_hw += grade
                counter += 1
        return round(sum_hw / counter, 2)

    def lecturer_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress or\
                course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        i = self.average_grade() < other.average_grade()
        return i

    def __eq__(self, other):
        i = self.average_grade() == other.average_grade()
        return i

    def __le__(self, other):
        i = self.average_grade() <= other.average_grade()
        return i

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturer_list.append(self)

    def average_grade(self):
        sum_hw = 0
        counter = 0
        for course in self.grades.values():
            for grade in course:
                sum_hw += grade
                counter += 1
        return round(sum_hw / counter, 2)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.average_grade()}'
        return res

    def __lt__(self, other):
        i = self.average_grade() < other.average_grade()
        return i

    def __eq__(self, other):
        i = self.average_grade() == other.average_grade()
        return i

    def __le__(self, other):
        i = self.average_grade() <= other.average_grade()
        return i


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        reviewer_list.append(self)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and \
                course in student.courses_in_progress or course in student.finished_courses:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}'
        return res


def stud_course_av_rate(course):
    all_rate = 0
    counter = 0
    for i in student_list:
        if course in i.grades.keys():
            for rate in i.grades[course]:
                all_rate += rate
                counter += 1
            return round(all_rate / counter, 2)
    else:
        return 'Оценок нет'


def lect_course_av_rate(course):
    all_rate = 0
    counter = 0
    for i in lecturer_list:
        if course in i.grades.keys():
            for rate in i.grades[course]:
                all_rate += rate
                counter += 1
            return round(all_rate / counter, 2)
    else:
        return 'Оценок нет'


student1 = Student('Ivan', 'Numberone', 'your_gender')
student1.courses_in_progress += ['Python', 'Unity']
student1.finished_courses += ['Git']
student2 = Student('Oleg', 'Doubleleg', 'your_gender')
student2.courses_in_progress += ['Python', 'Java']
student2.finished_courses += ['Git']

reviewer1 = Reviewer('Somen', 'Buddyn')
reviewer1.courses_attached += ['Git', 'Python', 'Java']
reviewer2 = Reviewer('Buddyn', 'Somen')
reviewer2.courses_attached += ['Unity', 'Python']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Git', 'Python']
lecturer2 = Lecturer('Buddy', 'Some')
lecturer2.courses_attached += ['Java', 'Unity']

student1.lecturer_rate(lecturer1, 'Git', 10)
student1.lecturer_rate(lecturer1, 'Git', 8)
student1.lecturer_rate(lecturer2, 'Unity', 8)
student1.lecturer_rate(lecturer2, 'Unity', 6)
student2.lecturer_rate(lecturer1, 'Python', 10)
student2.lecturer_rate(lecturer1, 'Python', 6)
student2.lecturer_rate(lecturer2, 'Java', 5)
student2.lecturer_rate(lecturer2, 'Java', 10)

reviewer1.rate_hw(student1, 'Git', 10)
reviewer1.rate_hw(student1, 'Git', 6)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 6)
reviewer1.rate_hw(student2, 'Java', 7)
reviewer1.rate_hw(student2, 'Java', 10)

reviewer2.rate_hw(student1, 'Unity', 9)
reviewer2.rate_hw(student1, 'Unity', 2)
reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 10)

for elem in student_list:
    print(elem, end='\n\n')

for elem in lecturer_list:
    print(elem, end='\n\n')

for elem in reviewer_list:
    print(elem, end='\n\n')

print(lecturer1 > lecturer2)
print(lecturer1 < lecturer2)
print(lecturer2 > lecturer1)
print(lecturer2 < lecturer1)
print(lecturer1 >= lecturer2)
print(lecturer1 <= lecturer2)
print(lecturer2 >= lecturer1)
print(lecturer2 <= lecturer1)
print(lecturer1 == lecturer2)
print(lecturer1 != lecturer2)
print()
print(stud_course_av_rate('Git'))
print(stud_course_av_rate('Python'))
print(stud_course_av_rate('Unity'))
print(stud_course_av_rate('Java'))
print(stud_course_av_rate('DataScience'))
print()
print(lect_course_av_rate('Git'))
print(lect_course_av_rate('Python'))
print(lect_course_av_rate('Unity'))
print(lect_course_av_rate('Java'))
print(lect_course_av_rate('DataScience'))
