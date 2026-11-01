students = []

# Create student
def create_student(data):

    student = {
        "id": len(students) + 1,
        "name": data.name,
        "age": data.age,
        "email": data.email,
        "course": data.course
    }

    students.append(student)

    return {
        "message": "Student created successfully",
        "data": student
    }


# Get all students
def get_all_students():

    return students


# Get student by ID
def get_student_by_id(student_id):

    for student in students:
        if student["id"] == student_id:
            return student

    return None


# Update student
def update_student(student_id, data):

    for student in students:
        if student["id"] == student_id:

            student["name"] = data.name
            student["age"] = data.age
            student["email"] = data.email
            student["course"] = data.course

            return student

    return None


# Delete student
def delete_student(student_id):

    for student in students:
        if student["id"] == student_id:

            students.remove(student)

            return True

    return False