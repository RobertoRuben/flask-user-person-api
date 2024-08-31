from flask import Flask
from src.config.connection_db import DatabaseConfig
from marshmallow import fields, ValidationError

app = Flask(__name__)
database_config = DatabaseConfig(app)
ma = database_config.get_ma()

class PersonDTO(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True, error_messages={"required": "El nombre es obligatorio."})
    paternal_surname = fields.String(required=True, error_messages={"required": "El apellido paterno es obligatorio."})
    maternal_surname = fields.String(required=True, error_messages={"required": "El apellido materno es obligatorio."})
    dni = fields.String(
        required=True,
        validate=lambda x: len(x) == 8 and x.isdigit(),
        error_messages={"required": "El DNI es obligatorio.", "validator_failed": "El DNI debe tener una longitud de 8 dígitos y contener solo números."}
    )

