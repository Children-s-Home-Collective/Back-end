from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_limiter import Limiter
from flask_limiter_util import get_remote_address
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()
ma = Marshmallow()
migrate=Migrate()
limiter= Limiter(key_func = get_remote_address)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(db, app)
    ma.init_app(app)
    limiter.init_app(app)
    jwt.init_app(app)
    CORS(app)

   
    from app.controllers.volunteer_controller import volunteer_bp
    from app.controllers.review_controller import review_bp
    from app.controllers.visit_controller import visitor_bp
    from app.controllers.user_controller import user_bp
    from app.controllers.auth_controller import auth_bp
    from app.controllers.donation_controller import donation_bp
    from app.controllers.children_home_controller import home_bp
    from app.controllers.admin_controller import admin_bp


    app.register_blueprint(volunteer_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(visitor_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(donation_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(admin_bp)

   
    @app.route('/')
    def home():
        return {"message": "Welcome to the API"}

    return app
