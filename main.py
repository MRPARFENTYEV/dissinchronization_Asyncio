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
from  models import StarwarsCharacter
import aiohttp
import  asyncio
import json
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


async def get_info(link:str, session:aiohttp.ClientSession):
    for i in range(1, 84):
        response = (link + str(i), session)
        json = await response.json()
        return json
async def main():
    async with aiohttp.ClientSession() as session:
        tasks.append(get_info())

        await asyncio.gather(*tasks)# распаковка
    save_data()

def save_data():
    pass






if __name__ == '__main__':
    asyncio.run(main())# вызов событийного цикла



