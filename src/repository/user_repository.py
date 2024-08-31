from src.models.entities.user_entity import UserEntity
from src.config.connection_db import db

class UserRepository:

    @staticmethod
    def get_all():
        return UserEntity.query.all()

    @staticmethod
    def get_by_id(user_id):
        return UserEntity.query.get(user_id)

    @staticmethod
    def add(user):
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update(user):
        db.session.commit()
        return user

    @staticmethod
    def delete(user):
        db.session.delete(user)
        db.session.commit()
        return user

    @staticmethod
    def exists(user_name):
        return db.session.query(db.exists().where(UserEntity.user_name == user_name)).scalar()
