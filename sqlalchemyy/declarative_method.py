from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import String, ForeignKey, create_engine, text
from sqlalchemy_utils import database_exists, create_database
import click
from pprint import pprint

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = "item"
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(30), nullable=False)
    price:Mapped[int]


class Shop(Base):
    __tablename__ = 'shop'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(String(30), nullable=False)
    address:Mapped[str] = mapped_column(String(255))

    def __repr__(self):
        return f'{self.id}, {self.name}, {self.address}'

    def __str__(self):
        return f'{self.id}, {self.name}, {self.address}'

    def __eq__(self, other):
        return self.id == other.id and self.name == other.name and self.address == other.address

class ItemShop(Base):
    __tablename__ = 'itemshop'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    shop_id:Mapped[int] = mapped_column(ForeignKey('shop.id'), nullable=False)
    item_id:Mapped[int] = mapped_column(ForeignKey('item.id'), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email:Mapped[str] = mapped_column(String(255))


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
        Item.metadata.create_all(bind=engine)
        ItemShop.metadata.create_all(bind=engine)
        Shop.metadata.create_all(bind=engine)
        Address.metadata.create_all(bind=engine)

    with Session(engine) as session:
        result = session.execute(text("SELECT * FROM shop"))
        pprint(result.fetchall())
if __name__ == '__main__':
    _create_database()

