from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from a JSON file
with open('q-vercel-python.json', 'r') as f:
    marks_data = json.load(f)

@app.get("/api")
async def get_marks(names: list[str]):
    result = []
    for name in names:
        if name in marks_data:
            result.append(marks_data[name])
        else:
            raise HTTPException(status_code=404, detail=f"Marks for {name} not found")
    return {"marks": result}
