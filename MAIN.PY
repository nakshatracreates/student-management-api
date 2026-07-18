from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

students=[]

class student(BaseModel):
    id:int
    name:str
    age:int
    email:str
    skills:list[str]

@app.post("/students")
def create_student(stud:student):
    students.append(stud)
    return {"messsage":"student created",
            "data":stud}

@app.get("/students")
def getall_student():
    return {"messsage":"student created",
            "data":students}

@app.get("/student/{student_id}")
def getone_student(student_id:int):
    for stud in students:
        if stud.id==student_id:
            return stud
    return {"student not found"}

@app.put("/student/{student_id}")
def update_student(student_id:int,updated_student:student):
    for index,stud in enumerate(students):
        if stud.id == student_id:
            students[index]=updated_student
            return update_student
    return{"message":"student not found"}

@app.delete("/student/{student_id}")
def delete_student(student_id:int):
    for index,stud in enumerate(students):
        if stud.id==student_id:
            students.pop(index)
            return{"message":"student deleted"}
    return {"error":"student not found"}


