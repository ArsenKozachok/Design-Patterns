from abc import ABC, abstractmethod

class Software:
    pass
class MobileApp:
    pass

class WebApp:
    pass

class DataBaseAPI:
    pass

class AndroidApp:
    pass

class IOSApp:
    pass

class PythonWeb:
    pass

class JSBackEndWeb:
    pass

class JSFrontEndWeb:
    pass

class Pipeline:
    pass

class TechStack(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def programming(self):
        pass
class Swift(TechStack):
    def __init__(self, name):
        super().__init__(name)

    def programming(self):
        return f'Swift'
class Python(TechStack):
    def __init__(self):
        super().__init__(name)

    def programming(self):
        return f'Python'
class JavaScript(TechStack):
    def __init__(self):
        super().__init__(name)

    def programming(self):
        return f'JavaScript'
class Party(ABC):
    def __init__(self, name, nubMembers, type):
        self.name = name
        self.nubMembers = nubMembers
        self.type = type
    @abstractmethod
    def add_member(self, *args):
        pass
class Member:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
class ScrumParty(Party):
    def __init__(self, name, nubMembers, type, member: Member):
        super().__init__(name, nubMembers, type)
        self.member = member
class adamParty(Party):
    def __init__(self, name, nubMembers, type, member: Member):
        super().__init__(name, nubMembers, type)
        self.member = member
    def add_member(self, *args):
        members = []
        members.append(Developer(developer.name, developer.surname,
                       developer.salary, developer.tech))
        for person in members:
            print(person.name, person.surname + " added", sep=' ')
class ScrumbanParty(Party):
    def __init__(self, name, nubMembers, type, member: Member):
        super().__init__(name, nubMembers, type)
        self.member = member
class Developer(Member):
    def __init__(self, name, surname, salary, tech):
        super().__init__(name, surname, salary)
        self._member = member
        self.tech = tech
    def work(self):
        self.tech.programming()
        return print(f'{self.name} {self.surname} {self.tech.name}')
class BusinessAnalyst:
    pass
class softArch(Developer):
    def __init__(self, name, surname, salary, tech, developer: Developer):
        super().__init__(name, surname, salary, tech)
        self.developer = developer
    def create_template(self):
        return print(f'{self.name} {self.surname} created')
    def read_clean_architecture(self):
        return f"{self.name} improved"
    def work(self, *args):
        self.developer.work()
class PartyLead(Developer):
    def __init__(self, name, surname, salary, tech, developer: Developer):
        super().__init__(name, surname, salary, tech)
        self.developer = developer
    def divide_and_rule(self):
        return f' busy'
    def work(self, *args):
        self.developer.work()
class QA:
    pass
member = Member('Adam', '1', 12345)
tech = Swift('Swift')
developer = Developer(name=member.name, surname=member.surname,
                      salary=member.salary, tech=tech)
d = softArch(name=member.name, surname=member.surname,
             salary=member.salary, tech=tech, developer=developer)
k = adamParty('Party', 6, 'Adam', member=member)
k.add_member()
d.create_template()
d.work()
d.read_clean_architecture()
