from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    
    app.config['SQLALCHEMY_DATABASE_URI'] = ''  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = ''  

    db.init_app(app)
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
