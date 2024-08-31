from flask import Flask
from src.config.connection_db import DatabaseConfig

app = Flask(__name__)
database_config = DatabaseConfig(app)
db = database_config.get_db()

class UserEntity(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)

    person_id = db.Column(db.Integer, db.ForeignKey('persons.id'), nullable=False)
    person = db.relationship('PersonEntity', back_populates="user")

    def __init__(self, user_name, password, person_id):
        self.user_name = user_name
        self.password = password
        self.person_id = person_id


