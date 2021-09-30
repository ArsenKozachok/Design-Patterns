"""
class Course
"""
from datetime import datetime


class CourseInfo:
    pass


class Course:
    """
    ...
    Attributes
    ----------
    name: str
    date: datetime
    seminars_number: int
    fee: float
    students[]

    """
    def __init__(self, id_: int, name: str, date: datetime, seminars_number: int, fee: float) -> None:
        self.name = name
        self.date = date
        self.seminars_number = seminars_number
        self.fee = fee
        self.student_id_list = []

    def __str__(self):
        return f"Course {self.name}..."

    def add_student(self, student_id: int) -> None:
        if isinstance(student_id, int) and student_id > 0:
            self.student_id_list.append(student_id)
            print(f"Student's id {student_id} has been added")
        else:
            raise ValueError('student id has to be int > 0')

    def remove_student(self, student_id: int) -> None:
        idx = -1
        for i, st_id in enumerate(self.student_id_list):
            if student_id == st_id:
                idx = i
                break
        # verify deletion if there is no idx == i
        if idx > -1:
            del self.student_id_list[idx]
