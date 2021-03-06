from dataclasses import dataclass
from datetime import datetime


@dataclass
class PersonalInfo:
    id: int
    name: str
    address: str
    phoneNum: str
    email: str
    position: str
    employedTime: datetime
