"""Simple program to check fastapi"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root()->dict:
    """
    root endpoint
     :return: returns as json object
    """
    return {"message": "Hello World"}

@app.get('/mypage')
def cus_index()->dict:
    """
    custom route
     :return: returns as json object with a message key
    """
    return "This is a custom message"