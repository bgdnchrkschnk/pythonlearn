import mysql.connector
import click


@click.command()
@click.option('--host', default="localhost", help='MySQL to connect to')
@click.option('--port', default=3306, help='MySQL to connect to')
@click.option('--username', help='Database username')
@click.option('--password', help='Database password')
@click.option('--database', help='Database to create')
def _insert_data(username,password,port,database,host):
    db_connector = mysql.connector.connect(username=username, password=password, port=port, database=database, host=host)
    cursor = db_connector.cursor()
    cursor.execute(
        "INSERT INTO Students (name, surname, age, profession, balance) VALUES ('Denis', 'Shpanchuk', 26, 'student', 0), ('Nikita', 'Simonyan', 24, 'student', 0)")
    db_connector.commit()

if __name__ == '__main__':
    _insert_data()