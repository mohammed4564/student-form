from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from controllers.student_controller import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student
)

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# Student form fields
class Student(BaseModel):
    name: str
    age: int
    email: str
    course: str


# Create student
@router.post("/create")
def add_student(data: Student):

    return create_student(data)


# Get all students
@router.get("/list")
def list_students():

    return get_all_students()


# Get student by ID
@router.get("/{student_id}")
def student_details(student_id: int):

    result = get_student_by_id(student_id)

    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return result


# Update student
@router.put("/update/{student_id}")
def edit_student(student_id: int, data: Student):

    result = update_student(student_id, data)

    if result is None:
        raise HTTPException(status_code=404, detail="Student not found")

    return result


# Delete student
@router.delete("/delete/{student_id}")
def remove_student(student_id: int):

    result = delete_student(student_id)

    if not result:
        raise HTTPException(status_code=404, detail="Student not found")

    return {"message": "Student deleted successfully"}