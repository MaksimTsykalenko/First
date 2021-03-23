from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import uvicorn
import api_v2

app = FastAPI()


class Show(BaseModel):
    ch_id: int
    start_t: datetime
    end_t: datetime


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/chanels/")
def read_chanels() -> list[dict]:
    return api_v2.get_chanels()


@app.get("/show/{ch_id}")
def read_shows(ch_id: str, start_t: Optional[str] = '1900-01-21 00:00:00',
               end_t: Optional[str] = '2900-01-21 00:00:00') -> list[dict]:
    try:
        show = Show(ch_id=ch_id, start_t=start_t, end_t=end_t)

    except:
        raise HTTPException(status_code=400, detail="400 Bad Request")

    return api_v2.get_shows(show.ch_id, show.start_t, show.end_t)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
