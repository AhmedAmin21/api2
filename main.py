from fastapi import FastAPI, Query
from pydantic import BaseModel

class BMIOutpt(BaseModel):
    bmi: float
    message: str

app = FastAPI()

@app.get("/")
def hi():
    return {'message': "hello"}

@app.get('/calculate_bmi')

def calculate_bmi(
    weight: int = Query(..., gt=20, lt=200, description='your weight in kg'), 
    height: int = Query(..., gt=100, lt=250, description='your height in cm')):

    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        message = 'underweight'
    elif 18.5 <= bmi < 25:
        message = 'normal'
    elif 25 <= bmi < 30:
        message = 'overweight'
    else:
        message = 'obese'
    
    return BMIOutpt(bmi=bmi, message=message)