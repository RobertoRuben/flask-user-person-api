from src.repository.person_repository import PersonaRepository
from src.models.entities.person_entity import PersonEntity
from src.models.dtos.person_dto import PersonDTO
from marshmallow import ValidationError

person_schema = PersonDTO()
persons_schema = PersonDTO(many=True)

class PersonaService:

    @staticmethod
    def get_all_personas():
        personas = PersonaRepository.get_all()
        return persons_schema.dump(personas)  # Serializa la lista de personas a JSON

    @staticmethod
    def get_persona_by_id(person_id):
        persona = PersonaRepository.get_by_id(person_id)
        return person_schema.dump(persona)

    @staticmethod
    def create_persona(data):
        # Validar los datos usando Marshmallow
        errors = person_schema.validate(data)
        if errors:
            raise ValidationError(errors)

        if PersonaRepository.exists(data['dni']):
            raise ValidationError(f"El DNI {data['dni']} ya existe.")

        new_persona = PersonEntity(
            name=data['name'],
            paternal_surname=data['paternal_surname'],
            maternal_surname=data['maternal_surname'],
            dni=data['dni']
        )
        persona = PersonaRepository.add(new_persona)
        return person_schema.dump(persona)

    @staticmethod
    def update_persona(person_id, data):

        persona = PersonaRepository.get_by_id(person_id)
        if persona:
            if data['dni'] and persona.dni != data['dni']:
                if PersonaRepository.exists(data['dni']):
                    raise ValidationError(f"El DNI {data['dni']} ya existe.")
                persona.dni = data['dni']

            persona.name = data['name']
            persona.paternal_surname = data['paternal_surname']
            persona.maternal_surname = data['maternal_surname']

            updated_persona = PersonaRepository.update(persona)
            return person_schema.dump(updated_persona)
        return None

    @staticmethod
    def delete_persona(person_id):
        persona = PersonaRepository.get_by_id(person_id)
        if persona:
            deleted_persona = PersonaRepository.delete(persona)
            return person_schema.dump(deleted_persona)
        return None
