from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse


from pymongo import MongoClient

app = FastAPI()



conn = MongoClient("mongodb+srv://satyam:sears%401234@cluster0.iwwk2.mongodb.net/notes")

