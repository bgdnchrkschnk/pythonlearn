import click
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from base import Base, DBExistError
from class_models import *


@click.command()
@click.option('--host', default="localhost", help='MySQL to connect to')
@click.option('--port', default=3306, help='MySQL to connect to')
@click.option('--username', help='Database username')
@click.option('--password', help='Database password')
@click.option('--database', help='Database to create')
def _create_database(host, port, username, password, database):
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{str(port)}/{database}')

    if not database_exists(engine.url):
        create_database(engine.url)
    else:
        raise DBExistError("This database is actually exist!")

    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    _create_database()