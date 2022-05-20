class Student:
    def __init__(self, name, surname, day, month, year, subjects):
        self.name = name
        self.surname = surname
        self.number = 0
        self.day = day
        self.month = month
        self.year = year
        self.subjects = subjects
        self.average = 0

    def show(self):
        print(f"[{self.number}]: {self.name} {self.surname} Rok urodzenia:{self.day}.{self.month}.{self.year}")
        print(" ".join("{}: {}".format(k, v) for k, v in self.subjects.items()))


class Diary:
    def __init__(self):
        self.students = list()
        self.number = 0

    def add_student(self, student):
        self.number = self.number + 1
        student.number = self.number
        self.students.append(student)
        self.students.sort(key=lambda x: x.surname)
        x = 1
        for student in self.students:
            student.number = x
            x = x + 1

    def update_one_grade(self, number, subject, grade):
        self.students[number - 1].subjects[subject] = grade

    def update_grade_subject(self, subject):
        if subject in self.students[0].subjects:
            for student in self.students:
                print(f"Zmiana/dodanie oceny oceny dla {student.number},{student.name},{student.surname} z {subject}")
                grade = input("Ocena:")
                if grade == "nie":
                    student.subjects[subject] = grade
                else:
                    grade = int(grade)
                    student.subjects[subject] = grade

        else:
            print("Nie ma podanego subjects w dzienniku")

    def dele_student(self, number):
        number = int(number)
        if number <= len(self.students):
            del self.students[number - 1]
            self.students.sort(key=lambda x: x.surname)
            self.students.sort(key=lambda x: x.name)
            x = 1
            for student in self.students:
                student.number = x
                x = x + 1
        else:
            print("Nie ma takiego ucznia o takim numberze")

    def add_subject(self, subject):
        for student in self.students:
            student.subjects[subject] = "brak oceny"

    def dele_subject(self, subject):
        if subject in self.students[0].subjects:
            for student in self.students:
                student.subjects.pop(subject)
        else:
            print("Nie ma takiego subjects")

    def show(self):
        for student in self.students:
            student.show()

    def list_subjects(self):
        subjects = {}
        for key in self.students[0].subjects.keys():
            subjects[key] = "brak oceny"
        return subjects

    def average_student(self):
        for student in self.students:
            print(f"[{student.number}]. {student.name} {student.surname} Srednia:")
            x = 0
            suma = 0
            for key in student.subjects:
                if student.subjects[key] == "brak oceny":
                    print("Nie ma wszystkich ocen")
                    break
                elif key == "religia" and student.subjects[key] == "nie":
                    suma = suma
                else:
                    suma = suma + student.subjects[key]
                    x = x + 1
            if len(student.subjects) == x:
                average = 0
                average = suma / x
                student.average = average
                print(round(average, 2))

    def average_class(self):
        print(self.average())

    def average(self):
        y = 0
        klasa = 0
        for student in self.students:
            x = 0
            suma = 0
            for key in student.subjects:
                if student.subjects[key] == "brak oceny":
                    break
                elif key == "religia" and student.subjects[key] == "nie":
                    suma = suma
                else:
                    suma = suma + student.subjects[key]
                    x = x + 1
            if len(student.subjects) == x:
                average = suma / x
                student.average = round(average, 2)
            klasa = klasa + round(average, 2)
            y += 1
        return klasa / y

    def check_len(self):
        if len(self.students) > 3:
            return 3
        else:
            return len(self.students)

    def three_best(self):
        self.average()
        self.students.sort(key=lambda x: x.average, reverse=True)
        for x in range(self.check_len()):
            print((x+1), f":{self.students[x].name} {self.students[x].surname} Average:{self.students[x].average}")

        self.students.sort(key=lambda x: x.surname)
        self.students.sort(key=lambda x: x.name)

    def update_grad_subjects(self):
        number = input("Give a number from a diary for student's dla who's wanna change name:")
        number = int(number)
        if number <= len(self.students):
            for key in self.students[number - 1].subjects:
                grade = input(f"Give new mark to subjects {key}:")
                grade = int(grade)
                self.students[number - 1].subjects[key] = grade
        else:
            print("Given number isn't in diary")


class Base:
    def __init__(self, diary):
        self.diary = diary

    def start(self):
        while True:
            if not self.menu():
                break

    def menu(self):
        print(
            " 1-Dodaj ucznie\n 2-Usun ucznia\n 3-Dodaj subject\n 4-Usun subject\n 5-Wpisz/popraw ocene z subjects\n 6-Wypisz liste osob z ich srednimi\n 7-Wypisz average klasy\n 8-Wypisz trzy osoby z najlepsza averagemi\n 9-Wyjdz:")
        wybor = int(input(":"))
        if wybor == 1:
            new_student = self.add_student()
            self.diary.add_student(new_student)
            self.diary.show()
        elif wybor == 2:
            delete_student = self.delete_student()
            self.diary.dele_student(delete_student)
        elif wybor == 3:
            subject = input("Jaki subject dodac:")
            self.diary.add_subject(subject)
        elif wybor == 4:
            subject = input("Jaki subject usunac:")
            self.diary.dele_subject(subject)
        elif wybor == 5:
            print(
                "Poprawic,wprowadzic ocene:\na)jednej osobie,jedna ocene\nb)danemy subjectowi\nc)jednej osobie wszystkie oceny:")
            grade = input()
            if grade == "a":
                _number, _subject, _change = input(
                    "Najpierw number daynik,subject i grade. Odzielone wszystko przecinkiem:\n").split(",")
                _number = int(_number)
                _change = int(_change)
                self.diary.update_one_grade(_number, _subject, _change)
                self.diary.show()
            elif grade == "b":
                _subject = input("Podaj subject:")
                self.diary.update_grade_subject(_subject)
            elif grade == "c":
                self.diary.update_grad_subjects()
        elif wybor == 6:
            self.diary.average_student()
        elif wybor == 7:
            self.diary.average_class()
        elif wybor == 8:
            self.diary.three_best()
        elif wybor == 9:
            return False
        return True

    def add_student(self):
        _name, surname, _day, _month, _year = input(
            "Podaj name,surname oraz date urodzenia ucznia(data urodzenia po przecinkach)\n").split(",")
        _day = int(_day)
        _month = int(_month)
        _year = int(_year)
        subjects = self.diary.list_subjects()
        new_student = Student(_name, surname, _day, _month, _year, subjects)
        return new_student

    def delete_student(self):
        number_student = input("Podaj number daynika ucznia: ")
        return number_student


def main():
    subjects = {"polski": 3, "angielski": 4, "matematyka": 5}
    student1 = Student("Marek", "Matusz", 5, 3, 2020, subjects)
    subjects = {"polski": 5, "angielski": 5, "matematyka": 3}
    student2 = Student("Magdalena", "Duch", 4, 4, 2020, subjects)
    subjects = {"polski": 3, "angielski": 4, "matematyka": 2}
    student3 = Student("Iwona", "Matysz", 6, 7, 2020, subjects)
    subjects = {"polski": 2, "angielski": 2, "matematyka": 2}
    student4 = Student("Tomasz", "Kowalski", 5, 7, 2020, subjects)
    new_diary = Diary()
    new_diary.add_student(student1)
    new_diary.add_student(student2)
    new_diary.add_student(student3)
    new_diary.add_student(student4)
    menu = Base(new_diary)
    menu.start()


if __name__ == "__main__":
    main()
