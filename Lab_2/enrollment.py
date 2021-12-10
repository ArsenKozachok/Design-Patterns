from datetime import datetime

from course import Course


class Enrollment:
    def __init__(self, course: Course):
        self.marks = dict()
        self.course = course

    def avarageDate(self, dateTo: datetime) -> float:
        grades = []
        for date, grade in self.marks.items():
            if date <= dateTo:
                grades.append(grade)
        return sum(grades) / len(grades)

    def get_final_mark(self) -> float:
        totalSum = float(sum(self.marks.values()))
        return totalSum / len(self.marks)
