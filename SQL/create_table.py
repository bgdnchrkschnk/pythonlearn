import mysql.connector
import click

@click.command()
@click.option('--host', default='localhost', help='MySQL to connect to')
@click.option('--port', default=3306, help='MySQL to connect to')
@click.option('--username', default="root", help='Database username')
@click.option('--password', default="2445253aQ", help='Database password')
@click.option('--database', help='Database to create')
def create_database(host, port, username, password, database):
    db_connector = mysql.connector.connect(username=username, password=password, host=host, port=port, database=database)
    cursor = db_connector.cursor()

# Create shop table
    cursor.execute("""
    CREATE TABLE shop (
ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
NAME VARCHAR(150) NOT NULL, 
ADDRESS VARCHAR(250) NOT NULL
)
    """)

# Create item table
    cursor.execute("""
    CREATE TABLE item (
ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
NAME VARCHAR(250) NOT NULL, 
PRICE FLOAT NOT NULL
);
    """)

# Create intermediate table to store one item in multiple stores
    cursor.execute("""
    CREATE TABLE item_shop (
ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
SHOP_ID INT NOT NULL,
ITEM_ID INT NOT NULL,
FOREIGN KEY (SHOP_ID) REFERENCES shop(ID)
);
    """)
    db_connector.close()

if __name__ == "__main__":
    create_database()