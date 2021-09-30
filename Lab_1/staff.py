from dataclasses import dataclass

from course import Course
from enrollment import Enrollment


@dataclass
class PersonalInfo:
    first_name: str
    last_name:  str
    address: str


class Student:
    """
   ...
    Attributes
   ----------
    name: str
    address: str
    phone_number: str
    email: str
    student_number: int
    average_mark: float

    Methods
    ----------
    can_enroll(seminar: Course)
    taken_seminar()
    enroll()
    unroll()

    """

    def __init__(self, id_: int, name: str, address: str, phone_number: str, email: str, student_number: int):
        self.id = id_
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.student_number = student_number
        self.average_mark = average_mark
        self.enrollments = []

    def can_enroll(self, seminar: Course):
        pass

    def taken_courses(self) -> int:
        return len(self.enrollments)

    def enroll(self, course: Course) -> None:
        course.add_student(student_id=self.id)
        enrollment = Enrollment(course=course)
        self.enrollments.append(enrollment)

    def unroll(self, course_id: int) -> None:
        idx = -1
        for i, item in enumerate(self.enrollments):
            if item.course == course_id:
                item.course.remove_student(student_id=self.id)
                idx = i
                break
        # TODO: verify deletion
        del self.enrollments[idx]


class Professor:
    """
    ...
    Attributes
    ----------
    name: str
    address: str
    phone_number: str
    email: str
    salary: float

    """

    def __init__(self, name: str, address: str, phone_number: str, email: str, salary: float,
                 course: Course):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.salary = salary
        self.course = course

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, course: Course):
        self._course = course
