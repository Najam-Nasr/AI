# TASK 3:

class Learner:
    def __init__(self, student_name, roll_no):
        self.student_name = student_name
        self._score = 0
        self.roll_no = roll_no

    def assign_score(self, score):
        if score < 0 or score > 100:
            print("Marks out of range")
        else:
            self._score = score

    def fetch_score(self):
        return self._score

    def determine_grade(self):
        if self._score >= 90:
            return "A"
        elif self._score >= 80:
            return "B"
        elif self._score >= 70:
            return "C"
        elif self._score >= 60:
            return "D"
        else:
            return "F"


student_one = Learner("Najam", 123)
student_one.assign_score(95)
print(student_one.student_name, "Marks:", student_one.fetch_score(),
      "Grade:", student_one.determine_grade())

student_two = Learner("Ahmed", 124)
student_two.assign_score(85)
print(student_two.student_name, "Marks:", student_two.fetch_score(),
      "Grade:", student_two.determine_grade())
