from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import fetch as ff
import uvicorn

serches = []

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/search')
async def receive_integers(search:str):

    res = ff.searchcall(search)
    print(*res,sep="\n\n")
    return res

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
