from src.models.entities.person_entity import PersonEntity
from src.config.connection_db import db

class PersonaRepository:

    @staticmethod
    def get_all():
        return PersonEntity.query.all()

    @staticmethod
    def get_by_id(person_id):
        return PersonEntity.query.get(person_id)

    @staticmethod
    def add(person):
        db.session.add(person)
        db.session.commit()
        return person

    @staticmethod
    def update(person):
        db.session.commit()
        return person

    @staticmethod
    def delete(person):
        db.session.delete(person)
        db.session.commit()
        return person

    @staticmethod
    def exists(dni):
        return db.session.query(db.exists().where(PersonEntity.dni == dni)).scalar()
