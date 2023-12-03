# Необходимо выгрузить cледующие поля:
# id - ID персонажа
# birth_year
# eye_color
# films - строка с названиями фильмов через запятую
# gender
# hair_color
# height
# homeworld
# mass
# name
# skin_color
# species - строка с названиями типов через запятую
# starships - строка с названиями кораблей через запятую
# vehicles - строка с названиями транспорта через запятую
# Данные по каждому персонажу необходимо загрузить в любую базу данных.
# Выгрузка из апи и загрузка в базу должна происходить асинхронно.

import aiohttp
import asyncio
from more_itertools import chunked
import json
from models import init_db, People, Session
result =[]#герои
tasks =[]#асинхронные функции
link = 'https://swapi.dev/api/people/'
'''async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(1,84):
            tasks.append(get_info(link+str(i),session))
        await asyncio.gather(*tasks)# распаковка
    save_data()'''
'''async def get_info(link:str, session:aiohttp.ClientSession):
    pass'''
'''def save_data():
    pass

'''

CHUNK_SIZE = 10

async def paste_to_db(people):
    # print(people)
    async with Session() as session:
        people = [People(json=person) for person in people]
        session.add_all(people)
        await session.commit()

        # print(param['name'])
# async def paste_to_db(people):
#     async with Session() as session:
#         people =[People(json = person) for person in people]
#         session.add_all(people)
#         await session.commit()
async def get_person(person_id, session):
        response = await session.get(f'https://swapi.dev/api/people/{person_id}')
        json_string = await response.json()
        return json_string
# async def main():
#     async with aiohttp.ClientSession() as session:
#         for people_id_chunk in chunked(range(1,83),CHUNK_SIZE):
#             coros =[]
#             for people_id in people_id_chunk:
#                 coros.append(get_person(people_id,session))
#             result = await asyncio.gather(*coros)
#             await paste_to_db(result)


async def main():
    await init_db()
    async with aiohttp.ClientSession() as session:
        for people_id_chunk in chunked(range(1, 83), CHUNK_SIZE):
            coros = [get_person(people_id,session) for people_id in people_id_chunk]
            result = await asyncio.gather(*coros)
            await paste_to_db(result)
            # await  save_data(result)

        # tasks.append(get_info())

    #     await asyncio.gather(*tasks)# распаковка
    # save_data()








if __name__ == '__main__':
    asyncio.run(main())# вызов событийного цикла



