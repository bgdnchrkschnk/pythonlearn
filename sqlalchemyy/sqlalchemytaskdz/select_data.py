import click
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from class_models import *


@click.command()
@click.option('--host', default="localhost", help='MySQL to connect to')
@click.option('--port', default=3306, help='MySQL to connect to')
@click.option('--username', help='Database username')
@click.option('--password', help='Database password')
@click.option('--database', help='Database to create')
@click.option('--name', help='Database to create')
def _select_data(host, port, username, password, database, name:str):
    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{str(port)}/{database}')

    with Session(engine) as session:
        all = session.query(Student).filter(Student.name == name)
        print(all.all())
        session.close()

if __name__ == '__main__':
    _select_data()


