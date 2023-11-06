from fastapi import FastAPI, Request
from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

note = APIRouter()


@note.get("/notes")
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "title": doc["title"],
            "desc": doc["desc"],
            "important": doc["important"]
        })
    return newDocs



@note.post("/note")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict["important"] == "on" else False
    note = conn.notes.notes.insert_one(formDict)
    return {"success": True}

