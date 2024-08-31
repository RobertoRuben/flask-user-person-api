from flask import Flask
from src.config.connection_db import DatabaseConfig
from src.controllers.person_controller import person_blueprint
from src.controllers.user_controller import user_blueprint

app = Flask(__name__)
database_config = DatabaseConfig(app)
db = database_config.get_db()

app.register_blueprint(person_blueprint)
app.register_blueprint(user_blueprint)  # Registrar el blueprint de usuarios

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
