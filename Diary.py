class Diary(object):
    def __init__(self, class_name, list_of_students):
        self.class_name = class_name
        self.list_of_students = list_of_students

    def add_student_to_list(self, student):
        self.list_of_students.append(student)

    def print_class_name(self):
        print(self.class_name)

    def average_class_score(self):
        sum_of_scores = 0
        count = 0
        for student in self.list_of_students:
            for score in student.scores:
                sum_of_scores += score
                count += 1
        return sum_of_scores/count

    def count_sum_of_student_attendance(self, name_of_student):
        len(self.list_of_students[name_of_student].attendance)

