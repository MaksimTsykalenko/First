import psycopg2
import json


con = psycopg2.connect( 
  user="postgres", 
  password="1qaz2wsx", 
  host="127.0.0.1", 
  port="5432"
)
con.autocommit = True
cur = con.cursor()
cur.execute('CREATE DATABASE Test1;')
con.close()

con = psycopg2.connect(
  database="test1", 
  user="postgres", 
  password="1qaz2wsx", 
  host="127.0.0.1", 
  port="5432"
)
cur = con.cursor()
cur.execute("CREATE TABLE chanels (id integer primary key, title varchar , icon varchar , disabled BOOLEAN);")
cur.execute("CREATE TABLE shows (id bigint primary key, title varchar , description varchar , start_t timestamp, end_t timestamp,chanel_id integer);")
con.commit()



with open("d:\export.json","r", encoding="utf-8") as json_file:
    data = json.load(json_file)

for chanel in data['channels']:
    cur.execute ("INSERT INTO chanels (id,title,icon,disabled) VALUES (%s, %s, %s,%s)",
				(chanel["id"],chanel["title"],chanel["logo"],False))
    for show in chanel['epg']:
        cur.execute ("INSERT INTO shows (id,title,description,start_t,end_t,chanel_id) VALUES (%s, %s, %s,%s, %s, %s)",
					(show["id"],show["title"],show["description"],show["start"],show["end"],chanel["id"]))
        
con.commit()
con.close()    