import os
from dotenv import load_dotenv
import psycopg2
from pathlib import Path


# создаем б.д:  createdb -U postgres db_asinc_exercise
# conn = psycopg2.connect(database='db_asinc_exercise',user='postgres',password = 'Sqlzaebal'
# )
conn = psycopg2.connect(database=os.environ.get("NAME")[::],
                        user=os.environ.get("USER")[::],
                        password = os.environ.get("PASSWORD")[::]
)
with conn.cursor() as cur:
    cur.execute("CREATE TABLE  starwars(id SERIAL PRIMARY KEY,birth_year  );")

conn.close()
'''id - ID персонажа
birth_year
eye_color
films - строка с названиями фильмов через запятую
gender
hair_color
height
homeworld
mass
name
skin_color
species - строка с названиями типов через запятую
starships - строка с названиями кораблей через запятую
vehicles - строка с названиями транспорта через запятую'''