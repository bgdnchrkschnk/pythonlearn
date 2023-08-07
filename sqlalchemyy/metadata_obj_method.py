from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import click


meta = MetaData()

item_metadata = Table('item', meta,
                      Column('ID', Integer, primary_key=True, autoincrement=True),
                      Column('ITEM_NAME', String(150)),
                      Column('PRICE', Float)
                      )

shop_metadata = Table('shop', meta,
                      Column('ID', Integer, primary_key=True, autoincrement=True),
                      Column('NAME', String(150)),
                      Column('ADDRESS', String(250))
                      )

item_shop_metadata = Table('item_shop', meta,
                           Column('ID', Integer, primary_key=True, autoincrement=True),
                           Column('SHOP_ID', Integer, ForeignKey('shop.ID', ondelete='cascade')),
                           Column('ITEM_ID', Integer, ForeignKey('item.ID', ondelete='cascade'))
                           )


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
        meta.create_all(bind=engine)

if __name__ == '__main__':
    _create_database()