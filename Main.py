from Diary import Diary
from Student import Student

class Main(object):
    def __init__(self, student=None, attendance=[], scores=[]):
        self.a = "a"
        self.list_of_students = []
        self.student = student
        self.attendance = attendance
        self.scores = scores

    def main(self):
        print("Welcome in Diary")
        print("Press a to show instruction")
        self.a = "a"
        while self.a != "q":
            print("Enter instruction")
            self.a = raw_input()
            if self.a == 'i':
                print("i - instruction " + '\n' +
                      "c - create student and add to Diary " + '\n' +
                      "m - use method xyz " + '\n' +
                      "k - create class" + '\n' +
                      "q - exit ")
            elif self.a == 'c':
                print("creating student")
                print("fill student attendance ")
                self.attendance = eval(raw_input())
                print("fill student scores ")
                self.scores = eval(raw_input())
                self.student = Student("Rafal","Wiensko", self.scores, self.attendance)
                self.list_of_students.append(self.student)
            elif self.a == 'm':
                print("using method average scores of class")
                print("Average scores of class " + repr(klas.class_name) + " " + repr(klas.average_class_score()) )
            elif self.a == 'k':
                print("creating klass")
                klas = Diary("Technical Physyics year 3", self.list_of_students)


if __name__ == "__main__":
    main = Main()
    main.main()
