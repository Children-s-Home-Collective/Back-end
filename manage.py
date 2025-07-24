import os
from flask.cli import FlaskGroup
from dotenv import load_dotenv

from app import db
from app.__init__ import create_app
from app.models.user import User
from app.models.donation import Donation
from app.models.visit import Visit
from app.models.review import Review
from app.models.volunteer import Volunteer
from app.models.children_home import ChildrenHome

load_dotenv()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "User": User,
        "Donation": Donation,
        "Visit": Visit,
        "Review": Review,
        "Volunteer": Volunteer,
        "ChildrenHome": ChildrenHome,
    }


if __name__ == "__main__":
    cli()
