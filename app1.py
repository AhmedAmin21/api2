## For read we use ( GET ) method
## For create we use ( POST ) method
## For update we use ( PUT ) method
## For delete we use ( DELETE ) method
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


class Student(BaseModel):
    id:int
    name:str
    grade:int

students = [
    Student(id=1, name='Ahmed Amin', grade=5),
    Student(id=2, name='Ahmed Hassan', grade=2),
]


@app.get('/students/')
def read_student():
    return students

@app.post('/students/')
def create_student(New_Student: Student):
    students.append(New_Student)
    return New_Student

@app.put("/students/{student_id}")
def update_student(student_id:int, updated_student:Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return updated_student
    return {'error': 'Student not Found'}


@app.delete('/students/{student_id}')
def delete_student(student_id:int):
    for index, student in enumerate(students):
        if student.id == student_id:
            del students[index]
            return {'message': f'student {student_id} deleted'}
    return {'error student not found'}