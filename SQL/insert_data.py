import mysql.connector
import click

from helper import *

@click.command()
@click.option('--host', default='localhost', help='MySQL to connect to')
@click.option('--port', default=3306, help='MySQL to connect to')
@click.option('--username', default="root", help='Database username')
@click.option('--password', default="2445253aQ", help='Database password')
@click.option('--database', help='Database to create')
def insert_data(host, port, username, password, database):
    db_connector = mysql.connector.connect(username=username, password=password, port=port, database=database, host=host)
    cursor = db_connector.cursor()
    shops = read_csv("shops.csv")
    items = read_csv("items.csv")
    items_in_shops = read_csv("items_shops.csv")

    #Insert shops
    cursor.execute(form_insert_from_dict_tuple("shop", shops))
    # sql = '''INSERT INTO test.shop VALUES (1, "ATB", "Govorova")'''
    # cursor.execute(sql)
    db_connector.commit()

    # cursor.execute(f"SELECT * from test.shop")
    # print(cursor.fetchall())

    # #Insert items
    cursor.execute(form_insert_from_dict_tuple("item", items))
    db_connector.commit()


  #Now put the items into shops
    items_data_rows = []
    for item_in_shop in items_in_shops:
        item = items[item_in_shop['ITEM']]
        shop = shops[item_in_shop['SHOP']]
        print(item)
    #     cursor.execute("SELECT ID FROM item WHERE ITEM_NAME = %(item_name)s ",
    #                              {"item_name": item["ITEM_NAME"]})
    #     print(cursor.statement)
    #     item_id = int(cursor.fetchone()[0])
    #     print(item_id)
    #     cursor.execute("SELECT ID FROM shop WHERE NAME = %(shop_name)s AND ADDRESS = %(shop_address)s",
    #                              {"shop_name": shop["NAME"], "shop_address": shop["ADDRESS"]})
    #     shop_id = int(cursor.fetchone()[0])
    #
    #     print(cursor.statement)
    #     print(shop_id)
    #
    #     items_data_rows.append((shop_id, item_id))
    #
    # cursor.executemany("INSERT INTO item_shop (SHOP_ID, ITEM_ID) VALUES (%s, %s)", items_data_rows)
    # print(cursor.statement)
    # db_connector.commit()
    db_connector.close()


if __name__ == "__main__":
    insert_data()
