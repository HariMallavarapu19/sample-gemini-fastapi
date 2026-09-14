from fastapi import FastAPI
from google import genai
import os
from dotenv import load_dotenv
from pydantic import BaseModel


load_dotenv()
app=FastAPI()
api_key=os.getenv("GEMINI_KEY")

client=genai.Client(api_key=api_key)

class QuestionRequest(BaseModel):
    question:str

@app.post('/askai')
def askai(request:QuestionRequest):
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=request.question 
    )
    return {
        "answer":response.text
    }
