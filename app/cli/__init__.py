import click
from app.db import db
from flask.cli import with_appcontext


@click.command(name='create-db')
@with_appcontext
def create_database():
    db.create_all()