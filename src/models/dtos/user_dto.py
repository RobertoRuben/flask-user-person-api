from flask import Flask
from src.config.connection_db import DatabaseConfig
from marshmallow import fields, validates, ValidationError

app = Flask(__name__)
database_config = DatabaseConfig(app)
ma = database_config.get_ma()

class UserDTO(ma.Schema):
    id = fields.Integer(dump_only=True)
    user_name = fields.String(required=True, error_messages={"required": "El nombre de usuario es obligatorio."})
    password = fields.String(required=True, load_only=True, error_messages={"required": "La contraseña es obligatoria."})
    person_id = fields.Integer(required=True, error_messages={"required": "El ID de la persona es obligatorio."})

    @validates('user_name')
    def validate_user_name(self, value):
        if len(value) < 3:
            raise ValidationError("El nombre de usuario debe tener al menos 3 caracteres.")

    @validates('password')
    def validate_password(self, value):
        if len(value) < 8:
            raise ValidationError("La contraseña debe tener al menos 8 caracteres.")


