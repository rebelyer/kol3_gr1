class Student(object):
    def __init__(self, student_name, student_surname, scores=[0,0], attendance=[0,0]):
        self.student_name = student_name
        self.student_surname = student_surname
        self.attendance = attendance
        self.scores = scores

    def add_score(self, score):
        self.scores.append(score)

    def add_attendance(self, attended):
        self.attendance.append(attended)
