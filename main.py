class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def _class_ar(self):
        list_sum = sum(self.grades)
        list_avg = list_sum / len(self.grades)

    def rate_cl(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return print(f"Студенты: Имя:{self.name}, Фамилия:{self.surname}, Пол:{self.gender}")


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
        return print(f"Проверяющие: Имя:{self.name}, Фамилия:{self.surname}")


# проверка

# if __name__ == "__main__":
student1 = Student("Alla", "Pugacheva", "women")
student2 = Student("Igor", "Rurikovich", "men")
student1.__str__()
student2.__str__()

reviewer1 = Reviewer("Van", "Helsing")
reviewer1.__str__()

lecturer1 = Lecturer("Macheha", "Zlaya")
lecturer1.__str__()






