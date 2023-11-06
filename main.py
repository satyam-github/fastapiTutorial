from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes.note import note
from routes.student import student
from pymongo import MongoClient

app = FastAPI()

conn = MongoClient("mongodb+srv://satyam:sears%401234@cluster0.iwwk2.mongodb.net/notes")
print("mongodb connected")

app.include_router(note)
app.include_router(student)

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Hello Bigger Applications!"}
