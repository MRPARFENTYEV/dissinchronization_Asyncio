import os
from dotenv import load_dotenv
import psycopg2
from pathlib import Path


# создаем б.д:  createdb -U postgres db_asinc_exercise
# conn = psycopg2.connect(database='db_asinc_exercise',user='postgres',password = 'Sqlzaebal'
# )
# conn = psycopg2.connect(database=os.environ.get("NAME")[::],
#                         user=os.environ.get("USER")[::],
#                         password = os.environ.get("PASSWORD")[::]
# )
# with conn.cursor() as cur:
#     cur.execute("""CREATE TABLE IF NOT EXISTS starwars(id SERIAL PRIMARY KEY,
#      birth_year VARCHAR(40),
#      eye_color VARCHAR(40),
#      films VARCHAR(40),
#      gender VARCHAR(40),
#      hair_color VARCHAR(40),
#      height VARCHAR(40),
#      homeworld VARCHAR(40),
#      mass VARCHAR(40),
#      name VARCHAR(40),
#      skin_color VARCHAR(40),
#      species VARCHAR[],
#      starships VARCHAR[],
#      vehicles VARCHAR[]
#      """)
#     conn.commit()
#
# conn.close()
# def func(num):

