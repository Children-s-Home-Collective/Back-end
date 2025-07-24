from flask_jwt_extended import get_jwt_identity
from app.models.user import User

def get_current_user():
    user_id = get_jwt_identity()
    if user_id:
        return User.query.get(user_id)
    return None
