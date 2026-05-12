from flask import Flask
from app.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)

    # Registramos las rutas que creamos en user_routes
    app.register_blueprint(user_bp)

    return app