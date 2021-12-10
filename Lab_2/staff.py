from abc import ABC, abstractmethod
from typing import List

from course import Course, Seminar
from enrollment import Enrollment
from personalInfo import PersonalInfo


class Staff(ABC):
    def __init__(self, personalInf: PersonalInfo) -> None:
        self.enrollments = list()
        self.comments = None
        self._personalInf = personalInf

    @property
    def personalInf(self) -> PersonalInfo:
        return self._personalInf

    @personalInf.setter
    def personalInf(self, _personalInf: PersonalInfo) -> None:
        if isinstance(_personalInf, PersonalInfo):
            self._personalInf = PersonalInfo
        else:
            raise AttributeError(f"personalInf object must be of class Personal info")

    def seminars(self) -> List[Course]:
        courses = [enrollment.course
                   for enrollment in self.enrollments]
        return courses

    @abstractmethod
    def enroll(self, course: Course) -> None:
        pass

    @abstractmethod
    def calculate(self) -> float:
        pass

    @abstractmethod
    def violation(self, message: str) -> str:
        pass


class Student(Staff):

    def __init__(self, personalInf: PersonalInfo, year: int, studentId: int, lessons: int) -> None:
        super().__init__(personalInf=personalInf)
        self.id = studentId
        self.avgMark = 0.0
        self.year = year
        self.violations = list()
        self.enrollments = list()
        self.lessons = lessons

    def violation(self, message: str) -> str:
        self.violations.append(message)
        return message

    def workload(self) -> float:
        return self.lessons * 2.5

    def seminar(self, seminar: Seminar) -> None:
        pass

    def enroll(self, course: Course) -> None:
        course.add_student(studentId=self.id)
        enrollment = Enrollment(course=course)
        self.enrollments.append(enrollment)
        return print(f'{self.personalInf.name} enrolled {course.courseInf.title}')

    def unenroll(self, course: Course) -> None:
        idx = 0
        for i, enrollment in enumerate(self.enrollments):
            if enrollment.course.id == course.id:
                idx = i
                break
        self.enrollments[idx].course.\
            remove_student(studentId=self.id)
        del self.enrollments[idx]
        return print(f'{self.personalInf.name}unrolled{course.courseInf.title}')

    def asd(self, course: Course) -> bool:
        if self.avgMark >= 4.5:
            return True

    def __str__(self):
        return print(f"Name: {self._personalInf.name} \n"
                     f"Address: {self._personalInf.address} \n"
                     f"Phone number: {self._personalInf.phone_number} \n"
                     f"Email: {self._personalInf.email} \n"
                     f"Position: {self._personalInf.position} \n"
                     f"Employed year: {self.year}")


class PostStudent(Staff):

    def __init__(self, personalInf: PersonalInfo, salary: float, lessons: int) -> None:
        super().__init__(personalInf=personalInf)
        self.salary = salary
        self.subordinate = []
        self.lessons = lessons

    def addStudent(self) -> None:
        pass

    def violation(self, message: str) -> str:
        pass

    def calculate_workload(self) -> float:
        return self.lessons * 1.5

    def asd (self, course: Course) -> None:
        pass

    def __str__(self):
        return print(f"ID: {self._personalInf.id} \n"
                     f"Name: {self._personalInf.name} \n"
                     f"Address: {self._personalInf.address} \n"
                     f"Phone number: {self._personalInf.phone_number} \n"
                     f"Email: {self._personalInf.email} \n"
                     f"Position: {self._personalInf.position} \n"
                     f"Employed year: {self._personalInf.employed_year} \n"
                     f"Salary: {self.salary}")
