from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    users = db.relationship('Favourites', backref='user')

    def __repr__(self):
        return self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    skin_color = db.Column(db.String(50))
    hair_color = db.Column(db.String(50))
    eye_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(50))
    genre = db.Column(db.String(50))
    description = db.Column(db.String(2000))
    image = db.Column(db.String(3000), nullable=False)

    characters = db.relationship('Favourites', backref='characters')

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "skin_color": self.skin_color,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "genre": self.genre,
            "description": self.description,
            "image": self.image
        }

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(250), nullable=False, unique=True)
    class_name = db.Column(db.String(200))
    manufacturer = db.Column(db.String(200))
    cost = db.Column(db.String(200))
    length = db.Column(db.Float)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    velocity = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    consumable = db.Column(db.Integer)
    description = db.Column(db.String(2000))
    image = db.Column(db.String(3000), nullable=False)

    vehicles = db.relationship('Favourites', backref='vehicles')


    def __repr__(self):
        return self.model_name

    def serialize(self):
        return {
            "id": self.id,
            "model_name": self.model_name,
            "class_name": self.class_name,
            "manufacturer": self.manufacturer,
            "cost": self.cost,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            "velocity": self.velocity,
            "capacity": self.capacity,
            "consumable": self.consumable,
            "description": self.description,
            "image": self.image
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    weather = db.Column(db.String(200))
    diameter = db.Column(db.Integer)
    gravity = db.Column(db.Integer)
    population = db.Column(db.Integer)
    terrain = db.Column(db.String(250))
    water_surface = db.Column(db.Integer)
    description = db.Column(db.String(2000))
    image = db.Column(db.String(3000), nullable=False)

    planets = db.relationship('Favourites', backref='planets')


    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "weather": self.weather,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population,
            "terrain": self.terrain,
            "water_surface": self.water_surface,
            "description": self.description,
            "image": self.image
        }
    
class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    
    # planetsFav = db.relationship('Planets', back_populates='planets',foreign_keys=[planet_id])

    def __repr__(self):
        return self.user_id

    def serialize(self):
        return {
            "user_id": self.user_id,
            "character_name": self.character.name,
            "vehicle_name": self.vehicle.model_name,
            "planet_name": self.planet.name
        }