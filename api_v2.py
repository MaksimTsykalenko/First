from sqlalchemy import create_engine
from models import chanels_table, shows_table
from datetime import datetime

engine = create_engine('postgresql://postgres:1qaz2wsx@localhost/test2')


def get_chanels() -> list[dict]:

    with engine.connect() as conn:
        query = chanels_table.select().where(chanels_table.c.disabled == False)
        data = conn.execute(query).fetchall()

    response = []
    for chanel in data:
        response.append({'id': chanel[0], 'title': chanel[1]})
    conn.close()
    return response


def get_shows(ch_id: int, start_t: datetime, end_t: datetime) -> list[dict]:
    with engine.connect() as conn:
        query = shows_table.select().where(shows_table.c.chanel_id == ch_id).where(
            shows_table.c.start_t >= start_t).where(shows_table.c.end_t <= end_t)
        data = conn.execute(query).fetchall()

    response = []
    for show in data:
        response.append({'id': show[0], 'title': show[1], 'description': show[2], 'start': show[3], 'end': show[4]})
    conn.close()
    return response
