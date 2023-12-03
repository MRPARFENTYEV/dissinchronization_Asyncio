import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import JSON, String

# POSTGRES_DB = os.getenv('POSTGRES_DB', 'Asyncio')
POSTGRES_HOST = os.getenv('POSTGRES_HOST', 'localhost')
POSTGRES_PORT = os.getenv('POSTGRES_PORT', '5431')
POSTGRES_DB = os.getenv('POSTGRES_DB', 'db_asinc_exercise')
POSTGRES_USER = os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'Sqlzaebal')

PG_DSN = 'postgresql+asyncpg://postgres:Sqlzaebal@localhost:5432/async'
# PG_DSN = f'postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
engine = create_async_engine(PG_DSN)
Session = async_sessionmaker(engine, expire_on_commit=False)
# session = Session()
# session.close()


class Base(AsyncAttrs, DeclarativeBase):
    pass


class People(Base):
    __tablename__ = 'swapi_people'

    id: Mapped[int] = mapped_column(primary_key=True)
    json: Mapped[dict] = mapped_column(JSON,nullable=True)
    # birth_year: Mapped[str] = mapped_column(String)
    # eye_color: Mapped[str] = mapped_column(String)
    # films: Mapped[str] = mapped_column(String)
    # gender: Mapped[str] = mapped_column(String)
    # hair_color: Mapped[str] = mapped_column(String)
    # height: Mapped[str] = mapped_column(String)
    # homeworld: Mapped[str] = mapped_column(String)
    # mass: Mapped[str] = mapped_column(String)
    # name: Mapped[str] = mapped_column(String)
    # skin_color: Mapped[str] = mapped_column(String)
    # species: Mapped[dict] = mapped_column(JSON)
    # starships: Mapped[dict] = mapped_column(JSON)
    # vehicles: Mapped[dict] = mapped_column(JSON)




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
