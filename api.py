from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import Optional
from pydantic import BaseModel
import uvicorn
import psycopg2

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
    con = psycopg2.connect(
        database="test1",
        user="postgres",
        password="1qaz2wsx",
        host="127.0.0.1",
        port="5432"
    )
    cur = con.cursor()
    cur.execute('SELECT id,title FROM chanels WHERE disabled=False;')
    response = []

    for chanel in cur.fetchall():
        response.append({'id': chanel[0], 'title': chanel[1]})
    con.close()
    return response


@app.get("/show/{ch_id}")
def read_shows(ch_id: str, start_t: Optional[str] = '1900-01-21 00:00:00',
               end_t: Optional[str] = '2900-01-21 00:00:00') -> list[dict]:
    try:
        show=Show(ch_id=ch_id,start_t=start_t,end_t=end_t)

    except:
        raise HTTPException(status_code=400, detail="400 Bad Request")

    con = psycopg2.connect(
        database='test1',
        user='postgres',
        password='1qaz2wsx',
        host='127.0.0.1',
        port='5432'
    )
    cur = con.cursor()
    cur.execute(
        'SELECT id,title,description,start_t,end_t FROM shows WHERE chanel_id= %s and start_t > %s and end_t < %s',
        (show.ch_id, show.start_t, show.end_t))


    response = []
    for show in cur.fetchall():
        response.append({'id': show[0], 'title': show[1], 'description': show[2], 'start': show[3], 'end': show[4]})

    return response


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
