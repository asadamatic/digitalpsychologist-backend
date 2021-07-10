from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
import base64
import uvicorn
from prediction_knn import evaluate_stress
app = FastAPI()


class BrainSignals(BaseModel):
    raw_data: List[str]


@app.post("/analyze")
async def analyze_brain_signals(file: BrainSignals):
    print(len(file.raw_data))
   

    stress_level = evaluate_stress(file.raw_data)
    return{
        'stress_level': stress_level,
    }
