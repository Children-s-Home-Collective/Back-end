from flask.cli import FlaskGroup
from dotenv import load_dotenv
from app import create_app, db
from app.models.user import User
from app.models.donation import Donation
from app.models.visit import Visit
from app.models.review import Review
from app.models.volunteer import Volunteer
from app.models.children_home import ChildrenHome, Child, Photo

load_dotenv()

app = create_app()
cli = FlaskGroup(create_app=create_app)


if __name__ == "__main__":
    cli()
