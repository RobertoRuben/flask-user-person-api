from src.repository.user_repository import UserRepository
from src.models.entities.user_entity import UserEntity
from src.models.dtos.user_dto import UserDTO
from marshmallow import ValidationError
from argon2 import PasswordHasher

user_schema = UserDTO()
users_schema = UserDTO(many=True)
ph = PasswordHasher()

class UserService:

    @staticmethod
    def get_all_users():
        users = UserRepository.get_all()
        return users_schema.dump(users)

    @staticmethod
    def get_user_by_id(user_id):
        user = UserRepository.get_by_id(user_id)
        return user_schema.dump(user)

    @staticmethod
    def create_user(data):
        # Validar los datos usando Marshmallow
        errors = user_schema.validate(data)
        if errors:
            raise ValidationError(errors)

        if UserRepository.exists(data['user_name']):
            raise ValidationError(f"El nombre de usuario {data['user_name']} ya existe.")

        hashed_password = ph.hash(data['password'])

        new_user = UserEntity(
            user_name=data['user_name'],
            password=hashed_password,
            person_id=data['person_id']
        )
        user = UserRepository.add(new_user)
        return user_schema.dump(user)

    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_by_id(user_id)
        if user:
            if data['user_name'] and user.user_name != data['user_name']:
                if UserRepository.exists(data['user_name']):
                    raise ValidationError(f"El nombre de usuario {data['user_name']} ya existe.")
                user.user_name = data['user_name']

            # Solo hashear la nueva contraseña si se ha proporcionado
            if 'password' in data and data['password']:
                user.password = ph.hash(data['password'])

            user.person_id = data['person_id']

            updated_user = UserRepository.update(user)
            return user_schema.dump(updated_user)
        return None

    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_by_id(user_id)
        if user:
            deleted_user = UserRepository.delete(user)
            return user_schema.dump(deleted_user)
        return None
