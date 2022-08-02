class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return print(f"Студенты: Имя:{self.name}, Фамилия:{self.surname}, Пол:{self.gender}, "
                     f"Средняя оценка за домашние задания:, Курсы в процессе изучения: {self.courses_in_progress}, "
                     f"Завершенные курсы: {self.finished_courses} ")

    #расчёт средней оценки написать функцию
    def middle(self):
        pass

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    # def __init__(self, name, surname):
    #     self.grades = {}

    def _class_ar(self):
        list_sum = sum(self.grades)
        list_avg = list_sum / len(self.grades)

    def __str__(self):
        return print(f"Лекторы: Имя:{self.name}, Фамилия:{self.surname}")
        # .self.name, self.surname,round(self._class_ar(), 2)


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
        return print(f"Проверяющие: Имя:{self.name}, Фамилия:{self.surname}, Средняя оценка за лекции: ")


# проверка

# студенты:
student1 = Student("Alla", "Pugacheva", "women")
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Java']
student1.__str__()

student2 = Student("Igor", "Rurikovich", "men")
student2.__str__()

#проверяющие:
reviewer1 = Reviewer("Van", "Helsing")
reviewer1.courses_attached += ['Python']
reviewer1.rate_hw(student1, 'Python', 6)
reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Python', 10)
print(student1.grades)
reviewer1.__str__()

#лекторы:
lecturer1 = Lecturer("Macheha", "Zlaya")
lecturer1.__str__()






