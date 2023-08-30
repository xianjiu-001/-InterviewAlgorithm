import requests
from dataclasses import dataclass


@dataclass
class student:
    no: int
    student: str
    age: int


student1 = student(no=1, student="21223", age="25")
student2 = student(no=2, student="21223", age="25")
print(student2 == student1)
print(student2)
URL = {
    "phone_confirm": "https://zcxx.htj.pdd.net/api/v1/server/_stm"
}
