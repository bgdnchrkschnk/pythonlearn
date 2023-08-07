from sqlalchemy.orm import Session
from sqlalchemy import text, create_engine, or_
from pprint import pprint
from declarative_method import Shop

engine = create_engine("mysql+pymysql://root:2445253aQ@localhost:3306/test", echo=False)

# connection = engine.connect()
# result = connection.execute(text("SELECT * FROM shop"))

# with engine.connect() as connection:
#     result = connection.execute(text('select * from shop'))
#     pprint(result.all())
#     print(result.first())
#     print(type(result.first()[0]))
#     print(result.one())
#     print(result.scalar()) - число без тюплів, лістів
#     print((result.fetchmany(size=3)))

with Session(engine) as session:
    shops = session.query(Shop).filter(or_(Shop.name == "ATB", Shop.id == 5))
    [print(shop) for shop in shops]
    # [print(shop[0]) for shop in shops]
    # print(expected_shop in shops)
    # pprint(result.all())
    # pprint(result.first())
    # pprint(type(result.first()[0]))
    # pprint(result.one())
    # pprint(result.scalar()) - число без тюплів, лістів
    # pprint((result.fetchmany(size=3)))




