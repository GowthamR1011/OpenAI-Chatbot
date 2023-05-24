from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import chat,newChat


class Query(BaseModel):
    messageHistory: list
    prompt:str | None = None
    topic: list | None = None

class newQuery(BaseModel):
    messageHistory: list

app = FastAPI()

@app.get("/")
async def root():
    return { "Message":"Hello World"}


@app.post("/chat/")
async def chatbot(query : Query):
    res = chat(query)
    return res


@app.post("/newchat")
async def newChatBot(query:newQuery):

    res =  newChat(query)

    return res  