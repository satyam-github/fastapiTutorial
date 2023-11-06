from config.db import conn
from schemas.student import student_helper
from bson.objectid import ObjectId


# Retrieve all students present in the database
async def retrieve_students():
    students = []
    async for student in conn.notes.students.find():
        students.append(student_helper(student))
    return students


# Add a new student into to the database
async def add_student(student_data: dict) -> dict:
    student = await conn.notes.students.insert_one(student_data)
    new_student = await conn.notes.students.find_one({"_id": student.inserted_id})
    return student_helper(new_student)


# Retrieve a student with a matching ID
async def retrieve_student(id: str) -> dict:
    student = await conn.notes.students.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)


# Update a student with a matching ID
async def update_student(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    student = await conn.notes.students.find_one({"_id": ObjectId(id)})
    if student:
        updated_student = await conn.notes.students.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from the database
async def delete_student(id: str):
    student = await conn.notes.students.find_one({"_id": ObjectId(id)})
    if student:
        await conn.notes.students.delete_one({"_id": ObjectId(id)})
        return True