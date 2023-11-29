import os

from sqlalchemy import String, JSON
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

HOST = os.getenv('HOST', 'localhost')
PORT = os.getenv('PORT', '5432')
NAME = os.getenv('NAME', 'db_asinc_exercise')
USER = os.getenv('USER', 'postgres')
PASSWORD = os.getenv('PASSWORD', 'Sqlzaebal')

PG_DSN = f'postgresql+asyncopg://{USER}:{PASSWORD}@{HOST}/{NAME}'
engine = create_async_engine(PG_DSN)
Session = async_sessionmaker(engine, expire_on_commit=False)
session = Session()
session.close()


class Base(AsyncAttrs, DeclarativeBase):
    pass


class StarwarsCharacter(AsyncAttrs, DeclarativeBase):
    __tablename__ = 'StarWarsCharacter'

    id: Mapped[int] = mapped_column(primary_key=True)
    birth_year: Mapped[int] = mapped_column(String)
    eye_color: Mapped[int] = mapped_column(String)
    films: Mapped[int] = mapped_column(String)
    gender: Mapped[int] = mapped_column(String)
    hair_color: Mapped[int] = mapped_column(String)
    height: Mapped[int] = mapped_column(String)
    homeworld: Mapped[int] = mapped_column(String)
    mass: Mapped[int] = mapped_column(String)
    name: Mapped[int] = mapped_column(String)
    skin_color: Mapped[int] = mapped_column(String)
    species: Mapped[dict] = mapped_column(JSON)
    starships: Mapped[dict] = mapped_column(JSON)
    vehicles: Mapped[dict] = mapped_column(JSON)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# class StarwarsCharacter(AsyncAttrs,DeclarativeBase):
#     def __init__(self, birth_year:str,
#                  eye_color:str,
#                  films:str,
#                  gender:str,
#                  hair_color:str,
#                  height:str,
#                  homeworld:str,
#                  mass:str,
#                  name:str,
#                  skin_color:str,
#                  species:list[str],
#                  starships:list[str],
#                  vehicles:list[str]
#                  ):
#         self.birth_year = birth_year
#         self.eye_color = eye_color
#         self.films = films
#         self.gender = gender
#         self.hair_color = hair_color
#         self.height = height
#         self.homeworld = homeworld
#         self.mass = mass
#         self.name = name
#         self.skin_color = skin_color
#         self.species = species
#         self.starships = starships
#         self.vehicles = vehicles
#     def __str__(self)->str:
#        return self.name
