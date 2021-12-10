from datetime import datetime
from typing import List


class CourseInformation:
    def __init__(self, title: str, date: datetime,
                 semNumber: int, fee: float):
        self.title = title
        self.startDate = date
        self.semNumber = semNumber
        self.fee = fee


class Course:
    def __init__(self, _id: int, info: CourseInformation):
        self.id = _id
        self.info = info
        self.studentId = []
        self.seminar_list = []

    def add_student(self, student_id: int) -> None:
        self.studentId.append(student_id)

    def remove_student(self, student_id: int) -> None:
        idx = 0
        for i, student in enumerate(self.studentId):
            if student.id == student_id:
                idx = i
                break
        del self.studentId[idx]


class Seminar:
    def __init__(self, id_: int, title: str,
                 deadline: datetime, items: List[str],
                 status: float, course: str):
        self.id = id_
        self.title = title
        self.deadline = deadline
        self.items = items
        self.status = status
        self.course = course

    def impItm(self, itemName: str) -> str:
        if itemName in self.items:
            return f"{itemName} implemented"

    def addComment(self, message: str, person) -> None:
        person.comments.append(f'{self.title}: {message}')
