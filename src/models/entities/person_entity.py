from flask import Flask
from src.config.connection_db import DatabaseConfig

app = Flask(__name__)
database_config = DatabaseConfig(app)
db = database_config.get_db()

class PersonEntity(db.Model):
    __tablename__ = 'persons'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    paternal_surname = db.Column(db.String(50), nullable=False)
    maternal_surname = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(8), unique=True, nullable=False)

    user = db.relationship("UserEntity", uselist=False, back_populates="person")

    def __init__(self, name, paternal_surname, maternal_surname, dni):
        self.name = name
        self.paternal_surname = paternal_surname
        self.maternal_surname = maternal_surname
        self.dni = dni

