class StarwarsCharacter:
    def __init__(self, birth_year:str,
                 eye_color:str,
                 films:str,
                 gender:str,
                 hair_color:str,
                 height:str,
                 homeworld:str,
                 mass:str,
                 name:str,
                 skin_color:str,
                 species:list[str],
                 starships:list[str],
                 vehicles:list[str]
                 ):
        self.birth_year = birth_year
        self.eye_color = eye_color
        self.films = films
        self.gender = gender
        self.hair_color = hair_color
        self.height = height
        self.homeworld = homeworld
        self.mass = mass
        self.name = name
        self.skin_color = skin_color
        self.species = species
        self.starships = starships
        self.vehicles = vehicles
    def __str__(self)->str:
       return self.name