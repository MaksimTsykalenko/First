import json
import models
from sqlalchemy import create_engine

engine=create_engine('postgresql://postgres:1qaz2wsx@localhost/test2')


with open("d:\export.json","r", encoding="utf-8") as json_file:
    data = json.load(json_file)

chanels=[]
shows=[]

for chanel in data['channels']:
    chanels.append({'id':chanel["id"],'title':chanel["title"],'icon':chanel["logo"],'disabled':False})
    for show in chanel['epg']:
        shows.append({"id":show["id"],'title':show["title"],'description':show["description"],'start_t':show["start"], 'end_t':show["end"],'chanel_id':chanel["id"]})

with engine.connect() as conn:
    query = models.chanels_table.insert().values(chanels).returning(models.chanels_table)
    result = conn.execute(query).fetchall()

with engine.connect() as conn:
    query = models.shows_table.insert().values(shows).returning(models.shows_table)
    result = conn.execute(query).fetchall()