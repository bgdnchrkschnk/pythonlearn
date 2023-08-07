import mysql.connector
import click

@click.command()
@click.option('--host', default='localhost', help='MySQL to connect to')
@click.option('--port', default=3306, help='MySQL to connect to')
@click.option('--username', default="root", help='Database username')
@click.option('--password', default="2445253aQ", help='Database password')
@click.option('--database', help='Database to create')
def select_data(host, port, username, password, database):
   db_connector = mysql.connector.connect(username=username, password=password, port=port, database=database, host=host)
   cursor = db_connector.cursor()
   try:
sql = "SELECT * FROM test.shop"
cursor.execute(sql)
result = cursor.fetchall() - метод fetchall() поверне усі записи бази даних result = cursor.fetchone() - метод fetchone() поверне перший запис бази даних
result = cursor.fetchmany(size=3) - метод fetchmany(size=) поверне к-ть записів з бази (size=к-ть записів)
print(result)
except mysql.connector.Error as err:
print(err)
print("Error Code:", err.errno)
print("SQLSTATE", err.sqlstate)
print("Message", err.msg)

db_connector.close()



if __name__ == "__main__":
   insert_data()
