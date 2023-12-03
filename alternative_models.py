

from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker

import sqlalchemy as sq
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import JSON
PG_DSN = 'postgresql+asyncpg://postgres:Sqlzaebal@localhost:5432/async'
engine = create_async_engine(PG_DSN)
Session = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()

class StarwarsCharacter(AsyncAttrs,Base):
    __tablename__ = 'StarwarsCharacters'
    id = sq.Column(sq.Integer, primary_key=True)
    birth_year = sq.Column(sq.Text)
    eye_color = sq.Column(sq.Text)
    films = sq.Column(sq.Text)
    gender = sq.Column(sq.Text)
    hair_color = sq.Column(sq.Text)
    height = sq.Column(sq.Text)
    homeworld_ = sq.Column(sq.Text)
    mass = sq.Column(sq.Text)
    name = sq.Column(sq.Text)
    skin_color = sq.Column(sq.Text)
    specie = sq.Column(JSON)
    starships = sq.Column(JSON)
    vehicles = sq.Column(JSON)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # def __init__(self,id:, birth_year:str,
    #              eye_color:str,
    #              films:str,
    #              gender:str,
    #              hair_color:str,
    #              height:str,
    #              homeworld:str,
    #              mass:str,
    #              name:str,
    #              skin_color:str,
    #              species:list[str],
    #              starships:list[str],
    #              vehicles:list[str]
    #              ):
    #     self.id = id
    #     self.birth_year = birth_year
    #     self.eye_color = eye_color
    #     self.films = films
    #     self.gender = gender
    #     self.hair_color = hair_color
    #     self.height = height
    #     self.homeworld = homeworld
    #     self.mass = mass
    #     self.name = name
    #     self.skin_color = skin_color
    #     self.species = species
    #     self.starships = starships
    #     self.vehicles = vehicles
    # def __str__(self)->str:
    #    return self.name

def create_tables(engine):
    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)